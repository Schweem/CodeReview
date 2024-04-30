from django.urls import path 
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('posts/', views.posts, name='posts'),
    path('like/<int:id>/', views.like, name='like'),
] 