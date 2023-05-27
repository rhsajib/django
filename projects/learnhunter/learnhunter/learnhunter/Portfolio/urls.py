from django.urls import path
from. import views


urlpatterns = [
    
    path('', views.Portfolio, name='Portfolio')
]