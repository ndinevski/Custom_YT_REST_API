from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings
from .form import handle_form
from YT_API import refresh

# Create your views here.
def login(request):
    return render(request, 'login.html')

@login_required
def home(request):
    if request.method == 'POST':
        form = handle_form()
        settings.YOUTUBE_CHANNEL_ID = request.POST.get('handle')
        print(settings.YOUTUBE_CHANNEL_ID)
        refresh.reload_urlconf()
        return render(request, 'home.html', {'form': form})
    return render(request, 'home.html')

