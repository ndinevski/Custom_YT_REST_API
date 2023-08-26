from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings
from .form import handle_form
from YT_API import refresh
from django.shortcuts import redirect
import requests

# Create your views here.
def login(request):
    return render(request, 'login.html')

@login_required
def home(request):
    if request.method == 'POST':
        form = handle_form()
        channel_name = request.POST.get('handle')

        search_url = 'https://youtube.googleapis.com/youtube/v3/search'
        params = {
                'part': 'snippet',
                'q' : channel_name,
                'type' : 'channel',
                'key' : settings.YOUTUBE_DATA_API_KEY,
            }
        r = requests.get(search_url, params=params)
        channel_id = r.json()['items'][0]['id']['channelId']
        
        settings.YOUTUBE_CHANNEL_ID = channel_id
        settings.YOUTUBE_CHANNEL_NAME = r.json()['items'][0]['snippet']['channelTitle']

        refresh.reload_urlconf()
        settings.USER = request.user.username
        
        return redirect('http://127.0.0.1:8000/statistics')
    
    form = handle_form()
    return render(request, 'home.html', {'form': form})