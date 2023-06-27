from .models import Post
from django.views.generic import ListView, DetailView

from django.urls import path, include
from . import views


app_name = 'alex'

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('suggestion_list/', views.suggestion_list, name='suggestion_list'),
    path('suggestions/<int:suggestion_id>/vote/', views.vote, name='vote'),
    path('WebTest/', views.store, name='WebTest'),
    path('noplant/', views.noplant, name='noplant'),
    path('typical/', views.typical, name='typical'),
    path('evil/', views.evil, name='evil'),
    path('exgirl/', views.exgirl, name='exgirl'),
    path('blah/', views.blah, name='blah'),
    path('blog/',
        ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25], template_name="blog.html"
        )),
    path('blog/<int:pk>/',views.post, name='post'),
]
