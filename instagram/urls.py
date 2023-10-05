from django.urls import path

from .views import index,comments

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>',comments ,name='comment')
]
