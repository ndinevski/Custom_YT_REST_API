from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .get_videos import get_videos_by_views, get_videos_by_rating
from django.conf import settings

@api_view(['GET'])
def videos(request, handle, format=None):
    return Response({'videos_by_views': get_videos_by_views(handle), 'videos_by_rating': get_videos_by_rating(handle)})

@api_view(['GET'])
def videos_by_views(request, handle, format=None):
    return Response(get_videos_by_views(handle))

@api_view(['GET'])
def videos_by_rating(request, handle, format=None):
    return Response(get_videos_by_rating(handle))