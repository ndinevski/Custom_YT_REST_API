import requests
from django.conf import settings

# TOP 10 Videos by Rating
def get_videos_by_rating(handle):
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'

    params_search_rating = {
        'part': 'snippet',
        'channelId': handle,
        'key': settings.YOUTUBE_DATA_API_KEY,
        'maxResults': 10,
        'order': 'rating',
        'type': 'video',
    }
    video_ids_rating = []
    r_rating = requests.get(search_url, params=params_search_rating)

    results_rating = r_rating.json()['items']

    for result in results_rating:
        video_ids_rating.append(result['id']['videoId'])

    params_video_rating = {
        'key': settings.YOUTUBE_DATA_API_KEY,
        'part': 'snippet, statistics, contentDetails',
        'id': ','.join(video_ids_rating),
    }

    r_rating = requests.get(video_url, params=params_video_rating)

    results_rating = r_rating.json()['items']

    videos_rating = []
    for result in results_rating:
        video_data = {
            'title': result['snippet']['title'],
            'id': result['id'],
            'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
            'view_count': result['statistics']['viewCount'],
            'like_count': result['statistics']['likeCount'],
            'comment_count': result['statistics']['commentCount'],
            'thumbnail': result['snippet']['thumbnails']['high']['url'],
            'description': result['snippet']['description'],
        }
        videos_rating.append(video_data)
    
    return videos_rating

# TOP 10 Videos by Views
def get_videos_by_views(handle):
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'

    params_search_views = {
        'part': 'snippet',
        'channelId': handle,
        'key': settings.YOUTUBE_DATA_API_KEY,
        'maxResults': 10,
        'order': 'viewCount',
        'type': 'video',
    }

    video_ids_views = []
    r_views = requests.get(search_url, params=params_search_views)

    results_views = r_views.json()['items']

    for result in results_views:
        video_ids_views.append(result['id']['videoId'])

    params_video_views = {
        'key': settings.YOUTUBE_DATA_API_KEY,
        'part': 'snippet, statistics, contentDetails',
        'id': ','.join(video_ids_views),
    }

    r_views = requests.get(video_url, params=params_video_views)

    results_views = r_views.json()['items']

    videos_views = []

    for result in results_views:
        video_data = {
            'title': result['snippet']['title'],
            'id': result['id'],
            'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
            'view_count': result['statistics']['viewCount'],
            'like_count': result['statistics']['likeCount'],
            'comment_count': result['statistics']['commentCount'],
            'thumbnail': result['snippet']['thumbnails']['high']['url'],
            'description': result['snippet']['description'],
        }
        videos_views.append(video_data)
    
    return videos_views
