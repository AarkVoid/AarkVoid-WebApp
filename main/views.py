from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q

from aakaar_admin.models import AboutUs_Detail, Abouts_Topic, ServicePage_Detail, Founder, Founder_Details, Testimonial, ClientProjectType, \
    ClientWorkingType, ProjectRequest_Form

from services.models import Service

import datetime

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

    context = {
        'about_us': about_us,
        'about_topics': about_topics,
        'service_detail': service_detail,
        'services': services,
        'founders': founders,
        'founder_details': founder_details,
        'testimonials': testimonials,
        'client_project_types': client_project_types,
        'client_working_types': client_working_types
    }
    return render(request, 'main/index.html', context)

# About us View
def about_view(request):
    context = {}
    return render(request, 'main/about.html', context)

# Project View
def project_view(request):
    context = {}
    return render(request, 'main/projects.html', context)

# Contact View
def contact_view(request):
    context = {}
    return render(request, 'main/contact.html', context)

# ************************** API Working Function ************************
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
            
            # Convert date into datetime
            date = datetime.datetime.strptime(date, '%m/%d/%Y').date()

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
                date = date
                )

            project_form.save()
            return redirect('index_view')
    except Exception as e:
        print('Exception in get_project_ideas_request : ', e)
        return redirect('index_view')