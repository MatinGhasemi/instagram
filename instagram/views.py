from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views import View

from .models import Post,Comment,User


# def index(request):
#     posts = Post.objects.all().order_by('-created_time')
#     return render(request,'instagram/main.html',context={'posts':posts})

class Index(View):
    def get(self,request):
        try:    
            posts = Post.objects.all().order_by('-created_time')
            return render(request,'instagram/main.html',context={'posts':posts})
        except:
            return render(request,"instagram/error.html",{})

# def comments(request,id):
#     post = Post.objects.get(id=id)
#     comment = post.comment_set.all()
#     return render(request,'instagram/comment.html',context={'post':post , 'comment':comment})

class Comments(View):
    def get(self,request,id):
        try:
            post = Post.objects.get(id=id)
            comment = post.comment_set.all().order_by('-created_time')
            return render(request,'instagram/comment.html',context={'post':post , 'comment':comment})
        except:
            return render(request,"instagram/error.html",{})

    def post(self,request,id):
        post = Post.objects.get(id=id)
        user = User.objects.get(id=1)
        comment_body = request.POST['comment_body']
        comment = Comment.objects.create(body=comment_body,user=user,post=post)
        comment.save()

        return redirect(f'/{id}')

# def userPage(request):
#     user = User.objects.get(username='Matin')
#     user_post = user.post_set.all()
#     return render(request,'instagram/user-page.html',{'user':user ,'user_post':user_post})

class UserPage(View):
    def get(self,request):
        user = User.objects.get(username='Matin')
        user_post = user.post_set.all()
        return render(request,'instagram/user-page.html',{'user':user ,'user_post':user_post})
