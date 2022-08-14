from django.shortcuts import render

# Create your views here.

def register_view(request):
    context = {}
    return render(request, 'profile/sign-up.html', context)

def login_view(request):
    context ={}
    return render(request, 'profile/sign-in.html',context)