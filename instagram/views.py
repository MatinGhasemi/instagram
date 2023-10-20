from time import timezone
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views import View
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.contrib.auth import login,logout,authenticate

from .models import Post,Comment,User,UserProfile
from .forms import RegisterForm,UserProfileForm,PostCreateAndUpdate,UserUpdate


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
        comment_body = request.POST['comment_body']
        comment = Comment.objects.create(body=comment_body,user=request.user,post=post)
        comment.save()

        return redirect(f'/{id}')


# def userPage(request):
#     user = User.objects.get(username='Matin')
#     user_post = user.post_set.all()
#     return render(request,'instagram/user-page.html',{'user':user ,'user_post':user_post})

class UserPage(View):
    def get(self,request):
        profile = UserProfile.objects.get(user=request.user).picture.url
        user = request.user
        user_post = user.post_set.all()
        # user_pic = UserProfile.objects.get(user=user)
        return render(request,'instagram/user-page.html',{'user':user ,'user_post':user_post,'profile': profile}) #'user_pic':user_pic})


class EditProfile(View):
    def get(self,request):
        profile = UserProfileForm(instance=request.user.userprofile)

        return render(request,'instagram/edit-profile.html',{'form':profile})

    def post(self,request):
        profile = UserProfileForm(request.POST , request.FILES, instance=request.user.userprofile)
        if profile.is_valid(): 
            c = profile.save(commit=False)
            c.user = request.user
            c.save()
            
            return redirect('/user-page')
        
        return render(request,'instagram/edit-profile.html',{'form':profile})
        

class EditSpecification(View):
    def get(self,request):
        specification = request.user
        form = UserUpdate(instance=specification)

        return render(request,'instagram/edit-Specifications.html',{'form':form})

    def post(self,request):
        specification = request.user
        form = UserUpdate(request.POST,instance=specification)

        if form.is_valid():
            c = form.save(commit=False)
            c.user = request.user
            c.save()

            return redirect('/user-page')

        return render(request,'instagram/edit-Specifications.html',{'form':form})
    

class PostCreate(View):
    def get(self,request):
        post = PostCreateAndUpdate()
        return render(request,'instagram/post-create.html',{'post':post})
    
    def post(self,request):
        post = PostCreateAndUpdate(request.POST , request.FILES)
        
        if post.is_valid():
            c = post.save(commit=False)
            c.user = request.user
            c.save()

            return redirect('/')
        
        return render(request,'instagram/post-create.html',{'post':post})


class RegisterUser(View):
    def get(self,request):
        form = RegisterForm()
        return render(request,'instagram/register.html',{'form':form})
    
    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)

            return redirect('/')
        
        return render(request,'instagram/register.html',{'form':form})
        
    
class UpdatePost(View):
    def get(self,request ,pk):
        post = Post.objects.get(id=pk)
        form = PostCreateAndUpdate(instance=post)
        return render(request,'instagram/update-post.html',{'form':form,'post':post})
    
    def post(self,request,pk):
        post = Post.objects.get(id=pk)
        form = PostCreateAndUpdate(request.POST,request.FILES,instance=post)
        if form.is_valid():
            c = form.save(commit=False)
            c.user = request.user
            c.save()
            return redirect(f'/{pk}')
        
        return render(request,'instagram/update-post.html',{'post':form})