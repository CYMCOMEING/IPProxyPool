import redis as pyredis
from configs.configs import REDIS, MYSQL
from database.mysqlclient import MySQLClient
from logger import logger

# redis
try:
    ipredis = pyredis.StrictRedis(
        connection_pool=pyredis.ConnectionPool(
            host=REDIS['host'],
            port=REDIS['port'],
            db=1,  # redis-scrapy会使用0
            encoding='utf8',
            decode_responses=True
        )
    )
except Exception as e:
    logger.error("ride 初始化失败")


class ProxyMysql():
    def __init__(self) -> None:
        self.mysql_client = MySQLClient(host=MYSQL['host'],
                            port=MYSQL['port'],
                            user=MYSQL['user'],
                            password=MYSQL['password'],
                            database=MYSQL['db'])
        self.mysql_client.execute('''
        CREATE TABLE IF NOT EXISTS proxyip (
        id INT AUTO_INCREMENT PRIMARY KEY,
        ip VARCHAR(255) NOT NULL,
        enable BOOL NOT NULL,
        ctime DATETIME DEFAULT CURRENT_TIMESTAMP,
        uptime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        );
        ''', commit=True)

    def add(self, proxy):
        """
        proxy ip:port
        """
        try:
            insert_data = "INSERT INTO proxyip (ip, enable) VALUES (%s, %s)"
            data = (proxy, 1)
            self.mysql_client.execute(insert_data, data, commit=True)
        except Exception as e:
            print(e)

    def delete(self, proxy):
        query = "UPDATE proxyip SET enable = 0 WHERE ip = %s;"
        data = (proxy)
        self.mysql_client.execute(query, data, commit=True)

    def random(self):
        query = "SELECT ip FROM proxyip WHERE enable = 1 ORDER BY RAND() LIMIT 1"
        self.mysql_client.execute(query)
        result = self.mysql_client.fetchone()
        return result
    
proxy_mysql = ProxyMysql()