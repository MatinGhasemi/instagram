from django.shortcuts import render

from .models import Post,Comment


def index(request):
    posts = Post.objects.all()
    return render(request,'instagram/main.html',context={'posts':posts})

def comments(request,id):
    post = Post.objects.get(id=id)
    comment = post.comment_set.all()
    return render(request,'instagram/comment.html',context={'post':post , 'comment':comment})