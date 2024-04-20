from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.executors.pool import ThreadPoolExecutor

from configs.configs import MONGODB
from logger import logger

RUN_JOBS = []

# 装饰器，用来添加任务到 RUN_JOBS
def add_jobs(func):
    RUN_JOBS.append(func)

mongostore = MongoDBJobStore(
    host=MONGODB['host'],
    port=MONGODB['port'],
    database='jobs',
    collection='cookies_pool_job'
)


scheduler = BackgroundScheduler(
    jobstroes={'default': mongostore},
    executors={'default': ThreadPoolExecutor(20)},
    job_defaults={'coalesce': False,
                  'max_instances': 3,
                  'misfire_grace_time': 3600
    },
    timezone='Asia/Shanghai',
    logger=logger
)

scheduler.start()


# 添加任务
from jobs.jobs import *

for f in RUN_JOBS:
    logger.info(f"package jobs.__init__.for RUN_JOBS: {f.__name__}")
    f()
