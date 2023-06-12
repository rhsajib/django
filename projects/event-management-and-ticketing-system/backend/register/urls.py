from django.urls import path
from . import views


app_name = "register"

urlpatterns = [
    path('create-user/', views.create_user_account, name='create_user_account'),
    path('api/create-user/', views.UserAPIView.as_view(), name='UserAPIView'),

    path('api-auth/user-index/', views.user_login, name='user_login'),
    # path('api-auth/user-index/', views.UserLoginAPIView.as_view(), name='UserLoginAPIView'),
    
    path('login/', views.login, name='login'),
    path('user-logout/', views.user_logout, name='logout'),
]
