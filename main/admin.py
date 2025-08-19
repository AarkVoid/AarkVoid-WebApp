from django.contrib import admin

from .models import CompanyDetail, SocialMedia,MainBannerContent,ContactSection,ContactInfoBox,AppSection,Feature

@admin.register(CompanyDetail)
class CompanyDetailAdmin(admin.ModelAdmin):
    list_display = ['companyName', 'companyEmail', 'companyMobile', 'companyAddress']

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['social_media_name', 'link']

@admin.register(AppSection)
class AppSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'app_section', 'order']

admin.site.register(MainBannerContent)
admin.site.register(ContactSection)
admin.site.register(ContactInfoBox)

