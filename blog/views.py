from django.shortcuts import render
from .models import Posts


def render_posts(request):
    posts = Posts.objects.all()
    return render(request, 'posts.html', {'posts': posts})
