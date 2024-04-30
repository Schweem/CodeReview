from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100) # Title of the post
    content = models.TextField() # Content of the post
    created_at = models.DateTimeField(auto_now_add=True) # Date and time of creation
    updated_at = models.DateTimeField(auto_now=True) # Date and time of last update ( if edit was here :) )
    likes = models.IntegerField(default=0) # Number of likes
    
    def __str__(self):
        return self.title