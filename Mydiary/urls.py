from django.contrib import admin
from django.urls import path
from .views import show,post_details,deletepost,editpost
urlpatterns = [
    path('',show, name='show'),
    path('<int:post_id>/', post_details, name='post_details'),
    path('<int:post_id>/delete',deletepost,name='deletepost'),
    path('<int:post_id>/edit',editpost,name='editpost'),
]
