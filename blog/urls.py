from django.urls import path
from . import views
from blog.views import (
    blog_post_list_view, 
    blog_post_detail_view,
    blog_post_delete_view,
    blog_post_update_view
)
urlpatterns = [
    path('',blog_post_list_view, name="home"),
    path('my-posts/',blog_post_list_view, name="user-posts"),
    path("<str:slug>/", blog_post_detail_view, name="detail"),
    path("<str:slug>/update/", blog_post_update_view, name="update"),
    path("<str:slug>/delete/", blog_post_delete_view, name="delete"),
    
]
