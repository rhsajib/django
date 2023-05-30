from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('', views.login_view, name = 'login_view')
]
