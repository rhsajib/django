from django.urls import path
from . import views

urlpatterns = [
    path('ml', views.machine),
    path('mm/', views.mymatch, name='mymatch')

]
