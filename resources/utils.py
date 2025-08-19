import random
from django.core.mail import send_mail
from django.conf import settings

from profiles.models import Profile, User_OTP

# Get profile Based on request or profile
def getProfile(request, profile=None):
    try:
        if not profile:
            profile = Profile.objects.get(user=request.user)
        else:
            profile = Profile.objects.get(user__username=profile)

    except Exception as e:
        profile =None
        print('Exception getProfile : ', e)

    return profile

def send_otp(request, profile):

    try:
        profileObj = getProfile(request, profile=profile)
        user_otp = random.randint(100000, 999999)

        if User_OTP.objects.filter(user=profileObj).exists():
            user_ = User_OTP.objects.filter(user=profileObj).last()
            user_.otp = user_otp 
            user_.save()
        else:
            user_ = User_OTP.objects.create(user=profileObj, otp=user_otp)
            user_.save()

        print('User OTP OBj : ', user_.user)
        message = f'Hello {profileObj.user.username.title()}, \n Your OTP is {user_otp}\n\nThankYou..\nAakaar Team'

        send_mail(
            f'Welcome to Aakaar Developers - Verify Your Email {profileObj.user.username.title()}',
            message,
            settings.EMAIL_HOST_USER,
            [profileObj.user.email],
            fail_silently = False
        )
    except Exception as e:
        print('Exception in Sending Email : ', e)

def otp_verification(request, profile_text, get_otp):
    profile = getProfile(request, profile=profile_text)

    # Check is OTP match or not
    if int(get_otp) == User_OTP.objects.filter(user=profile).last().otp:

        # Account is Active
        profile.user.is_active = True
        profile.user.save()
        return True
    
    return False