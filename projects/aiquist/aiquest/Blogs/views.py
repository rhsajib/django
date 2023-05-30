from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    h1_string = '<h2>Hi, you are inside blogs app !!!!!</h2>'
    return HttpResponse(h1_string)