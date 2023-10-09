from django.urls import path

from .views import index,comments,userPage

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>',comments ,name='comment'),
    path('user-page',userPage , name='userpage')
]
