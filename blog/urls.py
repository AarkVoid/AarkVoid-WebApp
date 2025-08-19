from django.urls import path
from .import views

urlpatterns = [
    path('', views.blog_view, name='blog_view'),
    path('blogDetails/<int:blog_id>/',views.Blog_details,name="Blog_details")
]
