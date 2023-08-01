from django.db import models
from django.conf import settings

# Create your models here.
class Statistics(models.Model):
    channel_id = models.CharField(max_length=100)
    date_and_time = models.CharField(max_length=100)
    subscriber_count = models.CharField(max_length=100)
    view_count = models.CharField(max_length=100)
    video_count = models.CharField(max_length=100)

    def __str__(self):
        return self.date_and_time