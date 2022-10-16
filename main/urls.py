from django.urls import path
from .import views

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('about/', views.about_view, name='about_view'),
    path('projects/', views.project_view, name='project_view'),
    path('contact/', views.contact_view, name='contact_view'),

    # API
    # Project Idea Request
    path('project_request/', views.get_project_ideas_request, name='get_project_ideas_request')
]