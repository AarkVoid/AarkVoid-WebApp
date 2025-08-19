from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect

from aakaar_admin.models import AboutUs_Detail, Abouts_Topic, ServicePage_Detail, Founder, Founder_Details, Testimonial, ClientProjectType, \
    ClientWorkingType, ProjectRequest_Form,projectPage,Project,Blog,BlogDetails,PricingPlan

from services.models import Service
from .models import MainBannerContent,ContactSection,AppSection,Feature

import datetime
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

# Homepage View

def index_view(request):

    # About Us Details
    try:
        about_us = AboutUs_Detail.objects.all().last()
        about_topics = Abouts_Topic.objects.all()
    except Exception as e:
        about_us = None
        about_topics = None
        print('Exception in about_us in index_view(): ', e)

    # Services Details
    try:
        service_detail = ServicePage_Detail.objects.all().last()
        services = Service.objects.all().order_by('?')[:6]
    except Exception as e:
        services = None
        service_detail = None
        print('Exception in services in index_view(): ', e)

    # Founders List
    try:
        founders = Founder.objects.all()
        founder_details = Founder_Details.objects.all().last()
    except Exception as e:
        founders = None
        founder_details = None
        print('Exception in services in index_view(): ', e)

    # Testimonial
    try:
        testimonials = Testimonial.objects.filter(Q(user__is_founder=False))
    except Exception as e:
        testimonials = None
        print('Exception in testimonials in index_view(): ', e)
    
    # Project Request Form
    try:
        client_project_types = ClientProjectType.objects.all().order_by('-created')
        client_working_types = ClientWorkingType.objects.all().order_by('-created')
    except Exception as e:
        client_project_type = None
        client_working_type = None
        print('Exception in client_project_type and client_working_type in index_view(): ', e)

    try:
        projectPageContent = projectPage.objects.all().last()
        DoneProjects = Project.objects.order_by('-created')[:6]
    except Exception as e:
        projectPageContent = None
        DoneProjects = None
        print('Exception in about_us in index_view(): ', e)
    
    try:
        blogs = Blog.objects.all()[:6] 
        blogcontent = BlogDetails.objects.all().last()
    except Exception as e:
        projectPageContent = None
        DoneProjects = None
        print('Exception in about_us in index_view(): ', e)

    try:
        plans = PricingPlan.objects.prefetch_related('features').all()
    except Exception as e:
        plans = None


    try:
        banner = MainBannerContent.objects.first()  # or filter by something
    except Exception as e:
        banner = None

    try:
        contacts = ContactSection.objects.prefetch_related('info_boxes').last()
    except Exception as e:
        print("Exception is :", e)
        contacts = None
    
    try:
        Appfeatures = AppSection.objects.prefetch_related('features').last()
    except Exception as e:
        Appfeatures = None

    print("Appfeatures :",Appfeatures)

    context = {
        'about_us': about_us,
        'about_topics': about_topics,
        'service_detail': service_detail,
        'services': services,
        'founders': founders,
        'founder_details': founder_details,
        'testimonials': testimonials,
        'client_project_types': client_project_types,
        'client_working_types': client_working_types,
        'projectData':projectPageContent,
        'Projects':DoneProjects,
        'Blogs':blogs,
        'blogcontent':blogcontent,
        'plans':plans,
        'banner':banner,
        "contact_section": contacts,
        "appfeatures":Appfeatures,
    }
    return render(request, 'main/index.html', context)

def update_banner(request):
    if request.method == 'POST':
        try:
            baId = request.POST.get("banner_id")
            print(" baId :",baId)
            banner = MainBannerContent.objects.get(id=baId)
            banner.small_heading = request.POST.get("banner_subtitle")
            banner.main_heading = request.POST.get("banner_head")
            banner.description = request.POST.get("banner_discription")
            banner.save()
        except Exception as e:
            print("Exception : ",e)
    return redirect('index_view')




# About us View
def about_view(request):
    try:
        about_us = AboutUs_Detail.objects.all().last()
        about_topics = Abouts_Topic.objects.all()
    except Exception as e:
        about_us = None
        about_topics = None
        print('Exception in about_us in index_view(): ', e)

     # Founders List
    try:
        founders = Founder.objects.all()
        founder_details = Founder_Details.objects.all().last()
    except Exception as e:
        founders = None
        founder_details = None
        print('Exception in services in index_view(): ', e)

    context = {'about_us': about_us,'about_topics': about_topics,'founders': founders,'founder_details': founder_details,}
    return render(request, 'main/about.html', context)




# Project View
def project_view(request):
    try:
        projectPageContent = projectPage.objects.all().last()
        DoneProjects = Project.objects.all()
    except Exception as e:
        projectPageContent = None
        DoneProjects = None
        print('Exception in about_us in index_view(): ', e)
    
    context = {'projectData':projectPageContent,'Projects':DoneProjects}
    return render(request, 'main/projects.html', context)

# Contact View
def contact_view(request):
    # Get contact section data
    try:
        contacts = ContactSection.objects.prefetch_related('info_boxes').last()
    except Exception as e:
        print("Exception is :", e)
        contacts = None
    
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone_number', '').strip()
        subject = request.POST.get('msg_subject', '').strip()
        message = request.POST.get('message', '').strip()
        
        # Validate inputs
        errors = []
        if not name:
            errors.append('Please enter your name')
        if not email or '@' not in email:
            errors.append('Please enter a valid email')
        if not message:
            errors.append('Please enter your message')
        
        if not errors:
            # Compose email
            email_subject = f"New Contact Form Submission: {subject}"
            email_body = f"""
            Name: {name}
            Email: {email}
            Phone: {phone}
            
            Message:
            {message}
            """
            
            try:
                # Send email (configure EMAIL_HOST in settings.py)
                send_mail(
                    subject=email_subject,
                    message=email_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,  # From email
                    recipient_list=[settings.CONTACT_RECEIVER_EMAIL,email,],  # To email(s)
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('contact_view')
            except Exception as e:
                errors.append(f'Failed to send message: {str(e)}')
        
        # If there are errors, add them to messages
        for error in errors:
            messages.error(request, error)
    
    context = {"contact_section": contacts}
    return render(request, 'main/contact.html', context)

# ************************** API Working Function ************************

# @csrf_protect
def get_project_ideas_request(request):
    try:
        # getting all form data via POST
        if request.method == 'POST':
            name = request.POST.get('client_name')
            email = request.POST.get('client_email')
            phone_number = request.POST.get('client_phone_number')
            project_type = request.POST.get('client_project_type')
            working_type = request.POST.get('client_working_type')
            date = request.POST.get('date')
            comments = request.POST.get('client_comment')
            
            # Convert date into datetime
            strptime_date = datetime.datetime.strptime(date, '%m/%d/%Y').date()
            date = datetime.datetime.strftime(strptime_date, '%Y-%m-%d')

            # get project type 
            project_type_obj = ClientProjectType.objects.get(pk=project_type)

            # get working type
            working_type_obj = ClientWorkingType.objects.get(pk=working_type)

            # Saving project details in database
            project_form = ProjectRequest_Form.objects.create(
                client_name = name, 
                client_email = email, 
                client_phone_number = phone_number,
                project_type = project_type_obj,
                working_type = working_type_obj,
                date = date,
                comments = comments
                )

            project_form.save()
            
            # ✅ Return JSON success
            return JsonResponse({"status": "success", "message": "Project request submitted successfully!"})
        else:
            return JsonResponse({"status": "error", "message": "Invalid request method"}, status=400)

    except Exception as e:
        print('Exception in get_project_ideas_request : ', e)
        return JsonResponse({"status": "error", "message": "Something went wrong"}, status=500)
    

