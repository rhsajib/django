from django.urls import path
from . import views


urlpatterns = [
    
    path('register/', views.Register, name='Register'),
    path('login/', views.Login, name='Login')
    
]