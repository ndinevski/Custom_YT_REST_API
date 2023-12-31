from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .serializers import StatsSerializer
from .models import Statistics
from . import get_statistics

# Create your views here.

# GET CURRENT CHANNEL STATISTICS
@api_view(['GET'])
def current_channel_stats(request, handle, format=None):
    if handle.endswith('.json'):
        handle = handle[:-5]
    data = get_statistics.current_statistics(handle)
    serializer = StatsSerializer(data=data)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)

# Can be added to add new statistic on every GET request, instead of using POST request
# GET ALL REFRESHED CHANNEL STATISTICS, IDs ordered chronologically
@api_view(['GET'])
def channel_stats(request, handle, format=None):
    statistics = Statistics.objects.filter(channel_id=settings.YOUTUBE_CHANNEL_ID).filter(user=settings.USER).order_by('-date_and_time')
    serializer = StatsSerializer(statistics, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

# UPDATE CHANNEL STATISTICS AND ADD CHANNEL STATISTICS OF THE CURRENT TIME
@api_view(['POST'])
def channel_stats_update(request, handle, format=None):
    data = get_statistics.current_statistics(handle)
    serializer = StatsSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# GET CHANNEL STATISTICS BY ID OR DELETE
@api_view(['GET', 'DELETE'])
def channel_stats_id(request,handle, id, format=None):
    try:
        statistic = Statistics.objects.filter(user=settings.USER).get(pk=id)
    except Statistics.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StatsSerializer(statistic)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        statistic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

# GET PARAMETERS FOR FRONTEND
@api_view(['GET'])
def variables(request, format=None):
    data = {
        'YOUTUBE_CHANNEL_ID': settings.YOUTUBE_CHANNEL_ID,
        'YOUTUBE_CHANNEL_NAME': settings.YOUTUBE_CHANNEL_NAME,
        'USER': settings.USER,
    }
    return Response(data, status=status.HTTP_200_OK)