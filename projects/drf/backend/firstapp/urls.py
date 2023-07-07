from django.urls import path
from . import views



urlpatterns = [
    path('first/', views.firstAPI, name = 'firstAPI'),
    path('registration/', views.registrationAPI, name = 'registrationAPI'),
    path('contact/', views.ContactAPIView.as_view(), name = 'ContactAPIView'),
    path('contactone/', views.ContactAPIViewOne.as_view(), name = 'ContactAPIViewOne'),
]
