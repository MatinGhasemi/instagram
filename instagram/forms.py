from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserProfile,Post,Comment


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True,max_length=255)

    class Meta:
        model= User
        fields = ['first_name','last_name','username','email','password1','password2']


class UserUpdate(forms.ModelForm):
    email = forms.EmailField(required=True,max_length=255)

    class Meta:
        model = User
        fields =  ['first_name','last_name','username','email']


class PostCreateAndUpdate(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['picture','post_body']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['picture']

