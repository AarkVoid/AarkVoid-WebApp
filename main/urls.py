from django.urls import path
from .import views

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('Update_banner/',views.update_banner,name="update_banner"),
    path('about/', views.about_view, name='about_view'),
    path('projects/', views.project_view, name='project_view'),
    path('contact/', views.contact_view, name='contact_view'),
    path('project_request/', views.get_project_ideas_request, name='get_project_ideas_request'),
]