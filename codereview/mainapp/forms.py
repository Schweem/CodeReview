from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta: 
        model = User # User model 
        fields = ['username', 'password1', 'password2'] # Fields to be displayed in the form

class LoginForm(forms.Form):
    username = forms.CharField() # Username field
    password = forms.CharField(widget=forms.PasswordInput) # Password field

class PostForm(forms.Form):
    title = forms.CharField() # Title field
    content = forms.CharField(widget=forms.Textarea) # Content field
