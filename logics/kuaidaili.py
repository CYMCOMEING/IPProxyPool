import requests
from bs4 import BeautifulSoup
from logger import logger
from configs.configs import configer, config_ini_file, HEADER_KUAIDILI, COOKIES_KUAIDILI


class KuaidailiPorxy:

    def __init__(self) -> None:
        self.index_url = 'https://www.kuaidaili.com/free/inha/{}/'

    def _get_url(self, url=None):
        try:
            resp  = requests.get('https://www.kuaidaili.com/free/', cookies=COOKIES_KUAIDILI, headers=HEADER_KUAIDILI)
        except Exception as e:
            logger.error('KuaidailiPorxy请求异常，{e}')
            
        if resp.status_code != 200:
            logger.warning(f"KuaidailiPorxy请求网页出错，请求码：{resp.status_code}")
            return ''
        logger.info(f"快代理IP获取成功，{url}")
        return resp.text
    
    def _parse_html(self, html=None):
        if not html:
            return
        
        soup = BeautifulSoup(html, 'lxml')
        proxies = []
        try:
            tbody = soup.find(class_='table table-bordered table-striped').tbody
            trs = tbody.find_all('tr')
            for tr in trs:
                # IP PORT 匿名度 类型 位置 响应速度 最后验证时间 付费方式
                ip = tr.find('td', attrs ={'data-title': 'IP'}).text
                port = tr.find('td', attrs ={'data-title': 'PORT'}).text
                proxies.append(f'{ip}:{port}')
            
        except Exception as e:
            logger.warning(f"kuaidili 解析网页出错，error:{e}")

        return proxies
    
    def get_porxy(self):
        curindex = configer.getint('kuaidili', 'curindex', fallback=1)
        
        proxies = []
        html = self._get_url(self.index_url.format(curindex))
        if html:
            proxies = self._parse_html(html)
            if proxies:
                configer.set('kuaidili', 'curindex', str(curindex+1))
                configer.write(open(config_ini_file, 'w'))
        
        return proxies