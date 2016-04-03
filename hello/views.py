from django.shortcuts import render
from django.http import HttpResponse
import urllib,m3u8
from .models import Greeting
# http://morning-shelf-20604.herokuapp.com/
# Create your views here.
def index(request):
    tv = m3u8.tv()
    tv2 = tv.tv_init()
    tv3 = tv.tv_load(tv2)
    return HttpResponse(tv2)
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

