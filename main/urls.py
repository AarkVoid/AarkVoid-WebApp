from django.urls import path
from .import views

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('about/', views.about_view, name='about_view'),
    path('projects/', views.project_view, name='project_view'),
    path('contact/', views.contact_view, name='contact_view')
]