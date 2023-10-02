from django.shortcuts import render

from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request,'instagram/main.html',context={'posts':posts})