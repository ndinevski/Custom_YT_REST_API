from apscheduler.schedulers.background import BackgroundScheduler
from .StatsUpdate import StatsUpdate


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(StatsUpdate.channel_stats_update(), 'interval', minutes=1)
    scheduler.start()