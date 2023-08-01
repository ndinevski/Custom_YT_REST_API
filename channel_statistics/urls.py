from django.urls import path
from . import views

urlpatterns = [
    path('', views.channel_stats, name='channel statistics'),
    path('', views.channel_stats_update, name='channel statistics update')
]
