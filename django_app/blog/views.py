from django.shortcuts import render
from .models import Post
def blog_home(request):
    posts = Post.objects.order_by("created_date")
    return render(request, 'blog/blog_home.html', {"posts": posts})

