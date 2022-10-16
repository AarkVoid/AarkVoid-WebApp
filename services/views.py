from django.shortcuts import render

from .models import Service, ServiceDetail ,SubCategoryService

# Services Page
def service_view(request):

    try:
        services = Service.objects.all().order_by('?')
    except Exception as e:
        services = None
        print('Exception in Service : ', e)

    context = {
        'services': services
    }
    return render(request, 'services/services.html', context)

# Services Details
def service_details(request, serviceId):
    serviceDetails = None 
    serviceSubcatogry = None

    try:
        serviceDetails = ServiceDetail.objects.get(id=int(serviceId))
        serviceSubcatogry = SubCategoryService.objects.filter(serviceName=serviceDetails.serviceName)
    except Exception as e:
        print('Exception in Service : ', e)

    context = {
        'serviceDetails': serviceDetails,
        'serviceSubcatogry': serviceSubcatogry
    }
    return render(request, 'services/services_details.html', context)