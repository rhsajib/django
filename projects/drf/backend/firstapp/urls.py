from django.urls import path
from . import views



urlpatterns = [
    path('first/', views.firstAPI, name = 'firstAPI'),
    path('registration/', views.registrationAPI, name = 'registrationAPI'),
]
