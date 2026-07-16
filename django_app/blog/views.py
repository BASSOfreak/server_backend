from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404

def blog_home(request):
    posts = Post.objects.order_by("created_date")
    return render(request, 'blog/blog_home.html', {"posts": posts})

def blog_entry(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/blog_entry.html', {'post': post})
