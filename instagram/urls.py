from django.urls import path

from .views import Index,Comments,UserPage

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('<int:id>',Comments.as_view() ,name='comment'),
    path('user-page',UserPage.as_view() , name='userpage')
]
