from django.shortcuts import render,get_object_or_404

from .models import Service, ServiceDetail
from aakaar_admin.models import ServicePage_Detail


# Services Page
def service_view(request):

    try:
        page_details = ServicePage_Detail.objects.all().last()
    except Exception as e:
        page_details = None
        print('Exception in service page details (Service_view): ', e)

    try:
        services = Service.objects.all().order_by('?')
    except Exception as e:
        services = None
        print('Exception in Service : ', e)

    context = {
        'page_details':page_details,
        'services': services,
    }
    return render(request, 'services/services.html', context)

# Services Details
def service_details(request, serviceId):
    
    try:
        service = Service.objects.get(id=serviceId)
        serviceDetails = ServiceDetail.objects.get(serviceName=service)
        ids = [serviceId-1,serviceId+1]
        allservices = Service.objects.filter(id__in=ids)
    except Exception as e:
        serviceDetails = None
        allservices = None

    print('serviceDetails: ', serviceDetails)
    context = {
        'serviceDetails': serviceDetails,
        'all_services':allservices,
    }
    return render(request, 'services/services_details.html', context)