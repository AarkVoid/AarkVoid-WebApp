from django.shortcuts import render, redirect
from django.conf import settings

import json
import requests

from .forms import UserCreationForm

# Create your views here.

def register_view(request):

    signUpForm = UserCreationForm()

    if request.method == 'POST':

        # Recaptcha Stuff
        client_key = request.POST.get('g-recaptcha-response')
        secret_key = settings.GOOGLE_CAPTCHA_SECRET_KEY

        # Captcha Data
        captcha_data = {
            'secret': secret_key,
            'response': client_key,
        }

        # Captcha Verification
        r = requests.post(settings.CAPTCHA_API_URL, data=captcha_data)
        response = json.loads(r.text)
        verify = response['success']

        if verify:
            signUpForm = UserCreationForm(request.POST or None)

            # Check if Form is Valid or Not
            if signUpForm.is_valid():
                # Saving user data is Database
                signUpForm.save()

                
        else:
            print('Please Verify Captcha!')
            redirect('index_view')

    context = {
        'form': signUpForm
    }
    return render(request, 'profile/sign-up.html', context)

def login_view(request):
    context ={}
    return render(request, 'profile/sign-in.html',context)