from django.shortcuts import render
from django.http import HttpResponse
import urllib,m3u8
from .models import Greeting

# Create your views here.
def index(request):
    vid = m3u8.load('http://dammikartmp.tulix.tv/slrc1/slrc1/playlist.m3u8')
    fl = list()
    for playlist in vid.playlists:
        if playlist.uri.rstrip().endswith('.m3u8'):
            sub = m3u8.load(playlist.uri)
            if sub.uri.rstrip().endswith('.ts'):
                fl.append(sub.uri)
        elif playlist.uri.rstrip().endswith('.ts'):
            fl.append(playlist.uri)
    return HttpResponse(str(fl))
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

