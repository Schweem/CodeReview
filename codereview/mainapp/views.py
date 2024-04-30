from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate # grab auth stuff 
from .models import Post # get post model 

from .forms import SignupForm, LoginForm, PostForm # get forms from forms 

# Register
def register(request): 
    if request.user.is_authenticated:  # If the user is already authenticated
        return redirect('posts')
    if request.method == 'POST': # If the request method is POST
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else: # If the request method is GET
        form = SignupForm()
    return render(request, 'register.html', {'form': form})

# Login
def login_user(request):
    if request.method == 'POST': # If the request method is POST
        form = LoginForm(request.POST)
        if form.is_valid(): # If the form is valid
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user: # If the user is authenticated
                login(request, user)    
                return redirect('posts')
    else: # If the request method is GET
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def posts(request):
    Posts = Post.objects.all()
    form = PostForm()
    if request.method == 'POST': # If the request method is POST
        form = PostForm(request.POST)
        if form.is_valid(): # If the form is valid
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            Post.objects.create(title=title, content=content)
            return redirect('posts') # Redirect to posts
        
    if request.method == 'GET': # If the request method is GET
        Posts = Post.objects.all()  # Get all the posts

    return render(request, 'posts.html', {'form': form, 'Posts': Posts})

def like(request, id):
    if request.method == 'POST': # If the request method is POST
        post = get_object_or_404(Post, id=id) # Get the post
        post.likes += 1  # Increment the likes
        post.save() # Save the post
    return redirect('posts') 