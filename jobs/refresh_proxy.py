from concurrent.futures import ThreadPoolExecutor
import requests

from logics.proxy import ProxyLogic
from configs.configs import HEADER_BAIDU, COOKIES_BAIDU
from logger import logger


executor = ThreadPoolExecutor(20)


class RefreshPorxyjob:

    @staticmethod
    def check_proxy(proxy, proxy_logic):
        '''检查代理是否能用'''
        host, port = proxy.split(':')
        proxyMeta = 'http://%(host)s:%(port)s' % {
            'host':host,
            'port':port,
        }
        use_proxy = {
            'http': proxyMeta,
            'https': proxyMeta,
        }
        try:
            url = "https://www.baidu.com"
            resp = requests.get(url, proxies=use_proxy, cookies=COOKIES_BAIDU, headers=HEADER_BAIDU, timeout=60)
            if resp.status_code != 200:
                proxy_logic.descrease(proxy)
                logger.warning(f'check_proxy 代理ip请求异常， ip: {proxy}')
            else:
                logger.info(f'check_proxy 代理ip请求正常， ip: {proxy}')
        except Exception as e:
            logger.warning(f'check proxy error, error:{e}')
            proxy_logic.descrease(proxy)

    @staticmethod
    def handle_proxy():
        '''代理池任务入口
        检查代理IP是否能用
        代理IP过少情况下去获取新的代理IP'''
        proxy_logic = ProxyLogic()
        proxies = proxy_logic.all()
        
        for proxy in proxies:
            executor.submit(RefreshPorxyjob.check_proxy, proxy, proxy_logic)
        if proxy_logic.count() < proxy_logic.need_num:
            proxy_logic.get_proxies()

    @staticmethod
    def run():
        '''代理池定时任务入口'''
        try:
            RefreshPorxyjob.handle_proxy()
        except Exception as e:
            logger.error(f"RefreshPorxyjob执行报错, error{e}")
