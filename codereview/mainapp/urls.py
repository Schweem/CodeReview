from django.urls import path 
from . import views

urlpatterns = [
    path('register/', views.register, name='register'), # URL for register
    path('login/', views.login_user, name='login'), # URL for login
    path('posts/', views.posts, name='posts'), # URL for posts
    path('like/<int:id>/', views.like, name='like'), # URL path for liking posts 
] 