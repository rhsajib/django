from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def machine(request):
    return HttpResponse('<h1>Welcome to Machine learning</h1>')

def mymatch(request):
    return HttpResponse('<h1>I am mymatch</h1>')