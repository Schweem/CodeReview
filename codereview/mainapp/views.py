from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import Post

from .forms import SignupForm, LoginForm, PostForm

# Register
def register(request):
    if request.user.is_authenticated:
        return redirect('posts')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'register.html', {'form': form})

# Login
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('posts')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def posts(request):
    Posts = Post.objects.all()
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            Post.objects.create(title=title, content=content)
            return redirect('posts')
        
    if request.method == 'GET':
        Posts = Post.objects.all() 

    return render(request, 'posts.html', {'form': form, 'Posts': Posts})

def like(request, id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=id)
        post.likes += 1  # Increment the likes
        post.save()
        return redirect('posts') 
    return redirect('login')