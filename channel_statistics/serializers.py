from rest_framework import serializers
from .models import Statistics

class StatsSerializer(serializers.ModelSerializer):
    channel_name = serializers.CharField(max_length=100, required=False)
    channel_id = serializers.CharField(max_length=100, required=False)
    date_and_time = serializers.CharField(max_length=100, required=False)
    subscriber_count = serializers.CharField(max_length=100, required=False)
    view_count = serializers.CharField(max_length=100, required=False)
    video_count = serializers.CharField(max_length=100, required=False)
    
    class Meta:
        model = Statistics
        fields = '__all__'