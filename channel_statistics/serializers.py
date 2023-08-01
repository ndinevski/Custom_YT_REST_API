from rest_framework import serializers

class StatisticsSerializer(serializers.Serializer):
    channel_id = serializers.CharField(max_length=100)
    date_and_time = serializers.CharField(max_length=100)
    subscriber_count = serializers.CharField(max_length=100)
    view_count = serializers.CharField(max_length=100)
    video_count = serializers.CharField(max_length=100)