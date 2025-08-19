from django.contrib import admin
from .models import AboutUs_Detail, Abouts_Topic, ServicePage_Detail, Maintenance_Detail, Maintenance_Topic, \
    Founder, Founder_Details, Testimonial, FounderSocialMedia, ClientProjectType, ClientWorkingType, ProjectRequest_Form, \
    projectPage,Project,Blog,BlogDetails,PricingPlan,PlanFeature

@admin.register(AboutUs_Detail)
class AboutUs_DetailAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created', 'updated']

@admin.register(Abouts_Topic)
class Abouts_TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon_label', 'created', 'updated']

@admin.register(ServicePage_Detail)
class ServicePage_DetailAdmin(admin.ModelAdmin):
    list_display = ['page_tile', 'page_head', 'created', 'updated']

@admin.register(Maintenance_Detail)
class Maintenance_DetailAdmin(admin.ModelAdmin):
    list_display = ['title', 'legend', 'description', 'created', 'updated']

@admin.register(Maintenance_Topic)
class Maintenance_TopicAdmin(admin.ModelAdmin):
    list_display = ['topic', 'created', 'updated']

@admin.register(Founder)
class FoundersAdmin(admin.ModelAdmin):
    list_display = ['user', 'created', 'updated']

@admin.register(Founder_Details)
class Founder_DetailsAdmin(admin.ModelAdmin):
    list_display = ['title', 'legend', 'description', 'created', 'updated']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['user', 'thoughts', 'enable', 'created', 'updated']

@admin.register(FounderSocialMedia)
class FounderSocialMediaAdmin(admin.ModelAdmin):
    list_display = ['social_media_name', 'link']

@admin.register(ClientProjectType)
class ClientProjectTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']

@admin.register(ClientWorkingType)
class ClientWorkingTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']

@admin.register(ProjectRequest_Form)
class ProjectRequest_FormAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'client_email', 'client_phone_number', 'project_type', 'working_type', 'date', 'created', 'updated']

@admin.register(projectPage)
class projectPage_Admin(admin.ModelAdmin):
    list_display = ['title','subtitle','text']

@admin.register(Project)
class Projects_Admin(admin.ModelAdmin):
    list_display = ['title','project_code','project_type','working_type','project_date']

@admin.register(Blog)
class Blog_Admin(admin.ModelAdmin):
    list_display = ['title','slug','date']

@admin.register(BlogDetails)
class BlogDetails_Admin(admin.ModelAdmin):
    list_display = ['title','updated']


admin.site.register(PricingPlan)
admin.site.register(PlanFeature)