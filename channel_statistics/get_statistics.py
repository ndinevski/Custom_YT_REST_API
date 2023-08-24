from django.conf import settings
import requests
from datetime import datetime

def current_statistics(handle):
    search_url = 'https://www.googleapis.com/youtube/v3/channels'
    params = {
            'part': 'statistics',
            'id': handle,
            'key' : settings.YOUTUBE_DATA_API_KEY,
        }
    r = requests.get(search_url, params=params)

    subscriber_count = r.json()['items'][0]['statistics']['subscriberCount']
    view_count = r.json()['items'][0]['statistics']['viewCount']
    video_count = r.json()['items'][0]['statistics']['videoCount']
    date_time = datetime.now()
    dt_string = date_time.strftime("%d/%m/%Y %H:%M:%S")
    channel_id = handle

    data= {"channel_id": channel_id,"date_and_time": dt_string , "subscriber_count": subscriber_count, "view_count": view_count, "video_count": video_count}
    return data