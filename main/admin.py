from django.contrib import admin

from .models import CompanyDetail, SocialMedia

@admin.register(CompanyDetail)
class CompanyDetailAdmin(admin.ModelAdmin):
    list_display = ['companyName', 'companyEmail', 'companyMobile', 'companyAddress']

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['social_media_name', 'link']