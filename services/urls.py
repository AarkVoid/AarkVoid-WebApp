from django.urls import path
from .import views

urlpatterns = [
    path('', views.service_view, name='service_view'),
    path('service_details/<str:serviceId>/', views.service_details, name='service_details'),
]