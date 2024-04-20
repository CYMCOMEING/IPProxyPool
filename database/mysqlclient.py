import pymysql
from threading import Lock
# from logger import logger


class MySQLClient:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.lock = Lock()
        self.connection = None
        self.cursor = None

        self.connect()

    def connect(self):
        try:
            self.connection = pymysql.connect(host=self.host,
                                    port=self.port,
                                    user=self.user,
                                    password=self.password,
                                    db=self.database,
                                    charset='utf8')
            self.cursor = self.connection.cursor()
        except Exception as e:
            # logger.error(f"Error connecting to MySQL: {e}")
            print(f"Error connecting to MySQL: {e}")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def execute(self, query, data=None, commit=False):
        with self.lock:
            try:
                self.cursor.execute(query, data)
                if commit:
                    self.connection.commit()
            except Exception as e:
                print(f"Error executing query: {e}")
            return self.cursor

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()
    
    def __del__(self):
        self.close()
