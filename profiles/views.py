from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

from .forms import CustomUserCreationForm, UserLoginForm
from .models import User_OTP
from .decorators import unauthenticate_user

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from resources.utils import send_otp, getProfile, otp_verification

import json
import requests

# Sign Up View : For registration
@unauthenticate_user
def register_view(request):
    """ Register View for User Signup """

    # Signup Form
    signUpForm = CustomUserCreationForm(label_suffix = " * ")

    # Request --> POST 
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

        # OTP Functionality
        get_otp = request.POST.get('otp')

        # OTP handing Statements
        if get_otp:

            profile_text = request.POST.get('user')
            verified = otp_verification(profile_text)
            if verified:
                messages.success(request, f'{profile_text.title()} Your Account is Created!!! Thanks For Registrations.')
                
                # Cookie for authentication
                if 'password_cookie' in request.session and 'username_cookie' in request.session:
                    username_session = request.session.get('username_cookie')
                    password_session = request.session.get('password_cookie')

                    # Authenticate user
                    user = authenticate(username=username_session, password=password_session)

                    # Logging in 
                    if user is not None:    
                        # User Login
                        login(request, user)
                        return redirect('index_view')                     
                else:
                    messages.warning(request, 'Account Verification Complete. Now Login to your account.')
                    return redirect('register_view')
            else:
                messages.warning(request, 'Your OTP Does Not Match... Your Entered Wrong OTP!')
                return render(request, 'profile/sign-up.html', {'otp': True, 'user': profile})

        # Captcha Verification : True 
        if verify:
            signUpForm = CustomUserCreationForm(request.POST or None)

            # Check if Form is Valid or Not
            if signUpForm.is_valid():

                # Saving user data is Database
                signUpForm.save()

                # Username
                username = signUpForm.cleaned_data.get('username').lower()

                # Storing Cookies for Authentication
                request.session['username_cookie'] = username
                request.session['password_cookie'] = signUpForm.cleaned_data.get('password1')

                # Sending OTP For Verification
                send_otp(request, username)
                return render(request, 'profile/sign-up.html', {'otp': True, 'profile': getProfile(request, profile=username)})
        else:
            messages.success(request, 'Captcha verification Pending.')
            return redirect('register_view')

    context = {
        'form': signUpForm,
    }
    return render(request, 'profile/sign-up.html', context)

# Log In View
@unauthenticate_user
def login_view(request):

    form = UserLoginForm()

    # getting post request data
    if request.method == 'POST':
        form = UserLoginForm(request.POST or None)

        otp = request.POST.get('otp')
        if otp:
            profile_text = request.POST.get('user')

            # Verify OTP and activate account
            verified = otp_verification(request, profile_text, otp)

            if verified:
                messages.success(request, f'{profile_text.title()} Your account is verified. you can login now.')
                return redirect('login_view')

        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username').lower(), password=form.cleaned_data.get('password'))

            if user is not None:
                # User Login
                login(request, user)

                # If next url is present.
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('index_view')
        
            # Check if user is exists or not
            elif not User.objects.filter(username=form.cleaned_data.get('username').lower()).exists():
                messages.info(request, 'User with this username does not exists.')
                print('User with this username does not exists.')
                return redirect('login_view')
            
            # if user exists than check is_active or not
            elif not User.objects.get(username=form.cleaned_data.get('username').lower()).is_active:
                profile = getProfile(request, profile=form.cleaned_data.get('username').lower())
                
                send_otp(request, profile.user.username)
                messages.warning(request, 'You need to verify your email with OTP!!!')
                return render(request, 'profile/sign-in.html', {'otp': True, 'profile': profile})

            # Password must be wrong
            else:
                messages.info(request, 'Password is incorrect')
                print('Password is incorrect')
                return redirect('login_view')

    context = {
        'form': form
    }
    return render(request, 'profile/sign-in.html', context)

# Profile View
@login_required
def profile_view(request):

    # get logged in profile
    profile = getProfile(request)

    context = {
        'profile': profile,
    }
    return render(request, 'profile/profile.html', context)

# Update Profile View
@login_required
def update_profile_view(request):

    # get logged in profile
    profile = getProfile(request)

    try:
        bankObj = BankDetails.objects.get(user=profile)
    except Exception as e:
        bankObj = None
        print('Exception in update_profile_view() : Bank Objects : ', e)
    
    try:
        addressObj = Address.objects.get(user=profile)
    except Exception as e:
        addressObj = None
        print('Exception in update_profile_view() : addressObj Objects : ', e)

    # UpdateProfile Form
    updateForm = UpdateProfileForm(instance=profile)
    bankUpdateForm = UpdateBankForm(instance=bankObj)
    addressUpdateFrom = UpdateAddressForm(instance=addressObj)

    context = {
        'updateForm': updateForm,
        'bankForm': bankUpdateForm,
        'addressForm': addressUpdateFrom
    }
    return render(request, 'profile/updateProfile.html', context)

# Log Out View
@login_required
def logout_view(request):
    logout(request)
    return redirect('login_view')