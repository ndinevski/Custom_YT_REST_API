from django.apps import AppConfig


class ChannelStatisticsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'channel_statistics'

    # TODO : FIX SCHEDULER
    # def ready(self):
    #     import os
    #     from . import jobs

        # RUN_MAIN check to avoid running the code twice since manage.py runserver runs 'ready' twice on startup
        # if os.environ.get('RUN_MAIN', None) != 'true':
        #     jobs.start()