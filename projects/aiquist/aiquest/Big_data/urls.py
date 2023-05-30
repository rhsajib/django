from django.urls import path 
from . import views

urlpatterns = [
    path('', views.big_data, name='bigdata'),
]