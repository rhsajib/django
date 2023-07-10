from django.urls import path
from . import views


app_name = 'session'
urlpatterns = [
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('sigup/', views.signup_user, name='signup_user'),
    path('changepass/', views.change_password, name='change_password'),  
]
