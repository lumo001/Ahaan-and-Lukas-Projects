from django.db import models

# blog/models.py
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    video = models.FileField(upload_to='videos/')
