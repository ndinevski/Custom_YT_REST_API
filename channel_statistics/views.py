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
from . import get_statistics

# Create your views here.

# GET CURRENT CHANNEL STATISTICS
@api_view(['GET'])
def current_channel_stats(request, handle, format=None):
    data = get_statistics.current_statistics(handle)
    serializer = StatsSerializer(data=data)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)

# Can be added to add new statistic on every GET request, instead of using POST request
# GET ALL REFRESHED CHANNEL STATISTICS, IDs ordered chronologically
@api_view(['GET'])
def channel_stats(request, handle, format=None):
    statistics = Statistics.objects.all()
    serializer = StatsSerializer(statistics, many=True)
    return Response({'statistics': serializer.data})

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
        statistic = Statistics.objects.get(pk=id)
    except Statistics.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StatsSerializer(statistic)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        # Statistics.objects.delete(pk=id)
        statistic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 