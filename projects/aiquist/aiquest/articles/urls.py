from django.urls import path
from . import views

# add an app_name to set the application namespace
app_name = "articles"

urlpatterns = [
    path('', views.articles_home, name ='articles_home'),
    path('<int:id>/', views.article_detail, name= 'article_detail'),
    path('random/<int:id>/', views.article_random_detail, name= 'article_random_detail'),
    path('search/', views.article_search_detail, name= 'article_search_detail'),
    path('create/', views.article_create, name= 'article_create'),
]