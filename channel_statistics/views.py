from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import requests
from .serializers import StatisticsSerializer
from .serializers import StatsSerializer
from datetime import datetime

# Create your views here.
# def statistics(request):
#     return render(request, 'index.html')

@api_view(['GET'])
def channel_stats(request):
    search_url = 'https://www.googleapis.com/youtube/v3/channels'
    params = {
            'part': 'statistics',
            'id': settings.YOUTUBE_CHANNEL_ID,
            'key' : settings.YOUTUBE_DATA_API_KEY,
        }
    r = requests.get(search_url, params=params)
    
    context = {
        'statistics': r.json()['items'][0]['statistics']
    }

    subscribers = r.json()['items'][0]['statistics']['subscriberCount']
    views = r.json()['items'][0]['statistics']['viewCount']
    videos = r.json()['items'][0]['statistics']['videoCount']

    date_time = datetime.now()
    dt_string = date_time.strftime("%d/%m/%Y %H:%M:%S")

    data= [{"channel_id": settings.YOUTUBE_CHANNEL_ID,"date_and_time": dt_string , "subscriber_count": subscribers, "view_count": views, "video_count": videos}]
    results = StatisticsSerializer(data, many=True)

    # return render(request, 'index.html', context)
    return JsonResponse(results.data, safe=False)

@api_view(['POST'])
def channel_stats_update(request):
    search_url = 'https://www.googleapis.com/youtube/v3/channels'
    params = {
            'part': 'statistics',
            'id': settings.YOUTUBE_CHANNEL_ID,
            'key' : settings.YOUTUBE_DATA_API_KEY,
        }
    r = requests.get(search_url, params=params)
    
    # context = {
    #     'statistics': r.json()['items'][0]['statistics']
    # }

    subscriber_count = r.json()['items'][0]['statistics']['subscriberCount']
    view_count = r.json()['items'][0]['statistics']['viewCount']
    video_count = r.json()['items'][0]['statistics']['videoCount']
    date_time = datetime.now()
    dt_string = date_time.strftime("%d/%m/%Y %H:%M:%S")
    channel_id = settings.YOUTUBE_CHANNEL_ID

    data= {"channel_id": channel_id,"date_and_time": dt_string , "subscriber_count": subscriber_count, "view_count": view_count, "video_count": video_count}
    serializer = StatsSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)