from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import requests
from .serializers import StatsSerializer
from datetime import datetime
from .models import Statistics

# Create your views here.

# GET ALL REFRESHED CHANNEL STATISTICS, IDs ordered chronologically
@api_view(['GET'])
def channel_stats(request):
    statistics = Statistics.objects.all()
    serializer = StatsSerializer(statistics, many=True)
    return JsonResponse({'statistics': serializer.data})

# UPDATE CHANNEL STATISTICS AND ADD CHANNEL STATISTICS OF THE CURRENT TIME
@api_view(['POST'])
def channel_stats_update(request):
    search_url = 'https://www.googleapis.com/youtube/v3/channels'
    params = {
            'part': 'statistics',
            'id': settings.YOUTUBE_CHANNEL_ID,
            'key' : settings.YOUTUBE_DATA_API_KEY,
        }
    r = requests.get(search_url, params=params)

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

# GET CHANNEL STATISTICS BY ID OR DELETE
@api_view(['GET', 'DELETE'])
def channel_stats_id(request, id):
    try:
        statistic = Statistics.objects.get(pk=id)
    except Statistics.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StatsSerializer(statistic)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        statistic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

# @api_view(['GET', 'POST'])
# def channel_stats(request):
#     if request.method == 'GET':
#         statistics = Statistics.objects.all()
#         serializer = StatsSerializer(statistics, many=True)

#     # return render(request, 'index.html', context)
#         return JsonResponse({'statistics': serializer.data})

#     if request.method == 'POST':
#         search_url = 'https://www.googleapis.com/youtube/v3/channels'
#     params = {
#             'part': 'statistics',
#             'id': settings.YOUTUBE_CHANNEL_ID,
#             'key' : settings.YOUTUBE_DATA_API_KEY,
#         }
#     r = requests.get(search_url, params=params)

#     subscriber_count = r.json()['items'][0]['statistics']['subscriberCount']
#     view_count = r.json()['items'][0]['statistics']['viewCount']
#     video_count = r.json()['items'][0]['statistics']['videoCount']
#     date_time = datetime.now()
#     dt_string = date_time.strftime("%d/%m/%Y %H:%M:%S")
#     channel_id = settings.YOUTUBE_CHANNEL_ID

#     data= {"channel_id": channel_id,"date_and_time": dt_string , "subscriber_count": subscriber_count, "view_count": view_count, "video_count": video_count}
#     serializer = StatsSerializer(data=data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
