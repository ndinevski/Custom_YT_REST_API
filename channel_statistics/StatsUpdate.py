from django.conf import settings
import requests
from .serializers import StatsSerializer
from datetime import datetime

class StatsUpdate():
    
    @staticmethod
    def channel_stats_update():
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