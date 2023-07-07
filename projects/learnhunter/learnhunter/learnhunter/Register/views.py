from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def Register(request):
    return render(request, 'register/register.html')


def Login(request):
    return render(request, 'register/login.html')