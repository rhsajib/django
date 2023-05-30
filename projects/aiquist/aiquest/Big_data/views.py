from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def big_data():
    return HttpResponse('<h1>I am from Big data</h1>')