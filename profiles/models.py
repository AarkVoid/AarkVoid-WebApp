from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
    # User information 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='Avatars', blank=True, null=True)
    middle_name = models.CharField(max_length=30)
    contact_number = models.IntegerField(blank=True, null=True)

    # Professional Info
    profession = models.CharField(max_length=30, blank=True, null=True)
    is_employed = models.BooleanField(default=False, blank=True, null=True)

    # Access Control
    is_founder = models.BooleanField(default=False, blank=True, null=True)
    
    def __str__(self):
        return str(self.user)