from django.contrib import admin
from .models import Service,ServiceDetail,SubCategoryService


# Register your models here.
@admin.register(Service)
class Service(admin.ModelAdmin):
    list_display = ['serviceName', 'serviceDescription','icon']


@admin.register(ServiceDetail)
class ServiceDetail(admin.ModelAdmin):
    list_display = ['serviceName', 'description']

@admin.register(SubCategoryService)
class SubCategoryService(admin.ModelAdmin):
    list_display = ['serviceName','SubCategoryName','description']