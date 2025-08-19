from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
    # User information 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='Avatars', blank=True, null=True, default='avatar.png')
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    contact_number = models.IntegerField(blank=True, null=True)

    # Professional Info
    profession = models.CharField(max_length=30, blank=True, null=True)
    is_employed = models.BooleanField(default=False, blank=True, null=True)

    # Access Control
    is_founder = models.BooleanField(default=False)
    is_verified_email = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.user)

# OTP handling Table
class User_OTP(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timeStamp = models.DateTimeField(auto_now_add=True)
    otp = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)