from rest_framework import serializers
from .models import Statistics

class StatisticsSerializer(serializers.Serializer):
    channel_id = serializers.CharField(max_length=100)
    date_and_time = serializers.CharField(max_length=100)
    subscriber_count = serializers.CharField(max_length=100)
    view_count = serializers.CharField(max_length=100)
    video_count = serializers.CharField(max_length=100)

class StatsSerializer(serializers.ModelSerializer):
    channel_id = serializers.CharField(max_length=100, required=False)
    date_and_time = serializers.CharField(max_length=100, required=False)
    subscriber_count = serializers.CharField(max_length=100, required=False)
    view_count = serializers.CharField(max_length=100, required=False)
    video_count = serializers.CharField(max_length=100, required=False)
    
    class Meta:
        model = Statistics
        fields = '__all__'