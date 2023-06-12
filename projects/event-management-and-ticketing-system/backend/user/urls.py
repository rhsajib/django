from django.urls import path
from . import views


app_name = "user"
urlpatterns = [
    path('home/', views.user_home, name='user_home'),
]
