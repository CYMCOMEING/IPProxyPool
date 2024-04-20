from jobs import scheduler, add_jobs
from jobs.refresh_proxy import RefreshPorxyjob

@add_jobs
def run_gushici_spider():
    # 触发一次，测试用
    # scheduler.add_job(RefreshPorxyjob.run,
    #                   trigger='date',
    #                   id='refresh_proxy',
    #                   run_date="2023-04-18 18:54:00",
    #                   replace_existing=True)
    scheduler.add_job(RefreshPorxyjob.run,
                      trigger='interval',
                      id='refresh_proxy',
                      minutes=30,
                      replace_existing=True)