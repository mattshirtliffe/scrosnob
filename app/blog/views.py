from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

from .models import Post

def index(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'blog/index.html',{'posts':posts})

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post.html',{'post':post})

def slug(request, slug):
    post = Post.objects.filter(slug=slug).first()
    if post:
        return render(request, 'blog/post.html',{'post':post})
    return HttpResponseNotFound('<h1>Page not found</h1>')
