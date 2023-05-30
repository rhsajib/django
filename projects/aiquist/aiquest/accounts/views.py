from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {
                'error' : 'Invalid username or password'
            }
            return render(request, 'accounts/login.html', context)
        print(user)
        login(request, user)
        return redirect('/articles')
    return render(request, 'accounts/login.html', {})