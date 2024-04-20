import requests
from bs4 import BeautifulSoup
from logger import logger
from configs.configs import configer, config_ini_file, HEADER_66IP, COOKIES_66IP


class Ip66Porxy:

    def __init__(self) -> None:
        self.index_url = 'http://www.66ip.cn/{}.html'

    def _get_url(self, url=None):
        try:
            resp = requests.get(url, cookies=COOKIES_66IP, headers=HEADER_66IP, verify=False)
        except Exception as e:
            logger.error('Ip66Porxy请求异常，{e}')
            
        if resp.status_code != 200:
            logger.warning(f"Ip66Porxy请求网页出错，请求码：{resp.status_code}")
            return ''
        logger.info(f"Ip66获取成功，{url}")
        return resp.text
    
    def _parse_html(self, html=None):
        if not html:
            return
        
        soup = BeautifulSoup(html, 'lxml')
        proxies = []
        try:
            soup = BeautifulSoup(html, 'lxml')
            proxies = []
            table = soup.find_all('table')[2]
            trs = table.find_all('tr')
            for tr in trs[1:]:
                # IP PORT 代理位置 代理类型 验证时间
                tds = tr.find_all('td')
                ip = tds[0].text
                port = tds[1].text
                proxies.append(f'{ip}:{port}')
            
        except Exception as e:
            logger.warning(f"ip66 解析网页出错，error:{e}")

        return proxies
    
    def get_porxy(self):
        curindex = configer.getint('ip66', 'curindex', fallback=1)
        
        proxies = []
        html = self._get_url(self.index_url.format(curindex))
        if html:
            proxies = self._parse_html(html)
            if proxies:
                configer.set('ip66', 'curindex', str(curindex+1))
                configer.write(open(config_ini_file, 'w'))
        
        return proxies