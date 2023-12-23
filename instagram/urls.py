from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import Index,Comments,UserPage,RegisterUser,EditProfile,PostCreate,UpdatePost,EditSpecification

urlpatterns = [
    path('', login_required(Index.as_view()), name='index'),
    path('<int:id>',login_required(Comments.as_view()) ,name='comment'),
    path('user-page/',login_required(UserPage.as_view()) , name='userpage'),
    path('edit-profile/',login_required(EditProfile.as_view()),name='edit-profile'),
    path('edit-Specifications/',login_required(EditSpecification.as_view()),name='edit-specifications'),
    path('post-create/',login_required(PostCreate.as_view()),name='post-create'),
    path('post-update/<int:pk>/',login_required(UpdatePost.as_view()),name='post-update'),
    path('accounts/register/',RegisterUser.as_view(),name='register')
]
