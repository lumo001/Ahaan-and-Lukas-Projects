from django.shortcuts import render
from .models import Post

# blog/views.py
def post_list(request):
    posts = Post.objects.all().order_by('-created_on')
    return render(request, 'blog/post_list.html', {'posts': posts})
