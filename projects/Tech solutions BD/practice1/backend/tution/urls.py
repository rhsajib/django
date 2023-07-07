from django.urls import path
from . import views


app_name = 'tution'
urlpatterns = [
    # path('contact/', views.contact_with_form, name='contact_with_form'),
    # path('contact/', views.contact_with_modelform, name='contact_with_modelform'),
    path('contact/', views.ContactView.as_view(), name='ContactView'),
    path('postlist/', views.PostListView.as_view(), name='PostListView'),
    # path('postdetail/<str:slug>/', views.PostsDetailView.as_view(), name='PostsDetailView'),
    path('postdetail/<int:pk>/', views.PostsDetailView.as_view(), name='PostsDetailView'),
    path('postdelete/<int:pk>/', views.PostDeleteView.as_view(), name='PostDeleteView'),
    path('postupdate/<int:pk>/', views.PostUpdateView.as_view(), name='PostUpdateView'),
    path('create/', views.PostCreateView.as_view(), name='PostCreateView'),
    path('posts/', views.postview, name='postview')

]
