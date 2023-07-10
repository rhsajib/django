from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from django.urls import reverse_lazy

from .forms import SignUpForm

# Create your views here.



def signup_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('session:login_user')
            
    form = SignUpForm()
    return render(request, 'session/signup.html', {'form': form})




def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('HomeView')
            
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('session:login_user')
    
    form = AuthenticationForm()
    return render(request, 'session/login.html', {'form': form})





def logout_user(request):
    logout(request)
    return redirect('session:login_user')




def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password successfully changed !!')
            return redirect('HomeView')
        
    form = PasswordChangeForm(request.user)
    return render(request, 'session/changepass.html', {'form':form})




