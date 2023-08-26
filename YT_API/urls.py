"""
URL configuration for YT_API project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, path, include
from django.contrib.auth import views as auth_views
from login import views as login_views
from videos import views as videos_views
from channel_statistics import views as statistics_views
from YT_API import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path("", login_views.home, name="home"),
    path('channel/<str:handle>', statistics_views.current_channel_stats, name='current channel statistics'),
    path('channel/<str:handle>/historical', statistics_views.channel_stats),
    path('channel/<str:handle>/historical/update', statistics_views.channel_stats_update),
    path('channel/<str:handle>/historical/<int:id>', statistics_views.channel_stats_id, name='channel statistics id'),
    path('channel/<str:handle>/videos/top10', include('videos.urls')),
    path('channel/<str:handle>/videos', videos_views.videos_json),
    path('channel/<str:handle>/videos_by_views', videos_views.videos_by_views),
    path('channel/<str:handle>/videos_by_rating', videos_views.videos_by_rating),
    re_path('(^(?!(admin|login|logout|social-auth|channel)).*$)',
    TemplateView.as_view(template_name="index.html")),
]

urlpatterns = format_suffix_patterns(urlpatterns)