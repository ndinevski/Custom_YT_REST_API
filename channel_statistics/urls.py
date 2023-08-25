from django.urls import path
from . import views

urlpatterns = [
    path('', views.channel_stats, name='channel statistics'),
    path('', views.channel_stats_update, name='channel statistics update'),
    path('', views.current_channel_stats, name='current channel statistics'),
    path('', views.channel_stats_id, name='channel statistics by id')
]
