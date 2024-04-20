import random
import threading
import requests
from database import ipredis, proxy_mysql
from logger import logger
from logics.kuaidaili import KuaidailiPorxy
from logics.ip66 import Ip66Porxy



class ProxyLogic:
    """
    代理相关逻辑
    
    每个IP初始有10分，连接失败扣一分，分数为零则删除
    用定时任务定时检测ip是否有效
    """

    def __init__(self) -> None:
        self.redis_kye = 'proxies'
        self.init_score = 10
        self.need_num = 5
        self.min_score = self.init_score - 5
        self.max_score = self.init_score
        self.session = requests.session()

    def get_proxies_from_zhima(self, num=10):
        '''从芝麻代理获取代理IP'''
        url = f'http://webapi.http.zhimacangku.com/getip?num={num}&type=2&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=2&regions='
        resp = self.session.get(url)
        resp = resp.json()
        proxies = []
        if resp.get('code', 0) == 0:
            data = resp.get('data', [])
            for d in data:
                ip = d.get('ip')
                port = d.get('port')
                proxies.append(f'{ip}:{port}')
            logger.info(f'请求芝麻代理IP. {data}')
        else:
            logger.error(f'请求芝麻代理失败， error{resp}')
        return proxies
    
    def get_proxies_from_kuaidili_free(self):
        '''从快代理获取代理IP'''
        kp = KuaidailiPorxy()
        proxies = kp.get_porxy()
        if not proxies:
            logger.warning(f'快代理请求IP为空')
        
        return proxies
    
    def get_proxies_from_ip66_free(self):
        '''从66IP代理获取代理IP'''
        kp = Ip66Porxy()
        proxies = kp.get_porxy()
        if not proxies:
            logger.warning(f'ip66代理请求IP为空')
        
        return proxies

    def get_proxies(self):
        '''获取代理写入myasql'''
        # proxies = self.get_proxies_from_zhima(3)
        # proxies = self.get_proxies_from_kuaidili_free()
        proxies = self.get_proxies_from_ip66_free()
        for proxy in proxies:
            self.add(proxy)
            proxy_mysql.add(proxy)
        return proxies

    def add(self, proxy):
        '''添加代理到redis'''
        if not ipredis.zscore(self.redis_kye, proxy):
            mapping = {proxy: self.init_score}
            return ipredis.zadd(self.redis_kye, mapping)
        
    def random(self):
        '''从redis随机获取代理IP'''
        proxies = ipredis.zrangebyscore(self.redis_kye, self.max_score, self.max_score)
        num = len(proxies)
        if num:
            if num < self.need_num:
                logger.warning(f'IP数量不足')
                threading.Thread(target=self.get_proxies).start() # 数量不足提前请求，尽量避免调用else的内容
        else:
            logger.warning(f'IP数量为零')
            proxies = self.get_proxies()  # 请求会阻塞
        if len(proxies):
            return random.choice(proxies)
        else:
            return ''
    
    def delete(self, proxy):
        '''redis删除代理IP'''        
        logger.info(f'rides zrem {self.redis_kye}: {proxy}')
        result = ipredis.zrem(self.redis_kye, proxy)
        return result

    def descrease(self, proxy):
        '''redis给代理IP减分''' 
        score = ipredis.zscore(self.redis_kye, proxy)
        # 扣分 or 删除
        if score and score > self.min_score:
            return ipredis.zincrby(self.redis_kye, -1, proxy)
        else:
            result = self.delete(proxy)
            proxy_mysql.delete(proxy)
            return result

    def count(self):
        '''返回redis中代理IP数量''' 
        return ipredis.zcard(self.redis_kye)
    
    def all(self):
        '''获取所有代理IP'''
        return ipredis.zrangebyscore(self.redis_kye, 0, 10)