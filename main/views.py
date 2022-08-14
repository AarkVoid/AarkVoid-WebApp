from django.shortcuts import render

def index_view(request):
    context = {}
    return render(request, 'main/index.html', context)

def about_view(request):
    context = {}
    return render(request, 'main/about.html', context)

def project_view(request):
    context = {}
    return render(request, 'main/projects.html', context)

def contact_view(request):
    context = {}
    return render(request, 'main/contact.html', context)