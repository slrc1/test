from django.shortcuts import render
from django.http import HttpResponse
import urllib
from .models import Greeting

# Create your views here.
def index(request):
    r = urllib.urlopen("http://nadeens.netau.net")
    return HttpResponse(r.read(10000))
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

