from django.shortcuts import render
from django.http import HttpResponse
import urllib,m3u8
from .models import Greeting

# Create your views here.
def index(request):
    vid = m3u8.load('http://dammikartmp.tulix.tv/slrc1/slrc1/playlist.m3u8')
    return HttpResponse(vid.playlists)
    sub = m3u8.load('http://dammikartmp.tulix.tv/slrc1/slrc1/'+vid.playlists[0].uri)
    fl = list()
    for playlist in sub.playlists:
        fl.append('http://dammikartmp.tulix.tv/slrc1/slrc1/'+playlist.uri)
        return HttpResponse(playlist.uri)
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

