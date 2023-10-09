from django.shortcuts import render

from .models import Post,Comment,User


def index(request):
    posts = Post.objects.all()
    
    return render(request,'instagram/main.html',context={'posts':posts})

def comments(request,id):
    post = Post.objects.get(id=id)
    comment = post.comment_set.all()
    return render(request,'instagram/comment.html',context={'post':post , 'comment':comment})

def userPage(request):
    user = User.objects.get(username='Matin')
    user_post = user.post_set.all()
    return render(request,'instagram/user-page.html',{'user':user ,'user_post':user_post})