from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse('<h2>Hi, you are inside blogs app</h2>')