from django.urls import path
from .views import post_list,create_post,update_post,delete_post

urlpatterns = [
    path('',post_list,name="post_list"),
    path('post/new',create_post,name="create_post"),
    path('post/<int:pk>/edit',update_post,name='update_post'),
    path('post/<int:pk>/delete',delete_post,name='delete_post'),
]