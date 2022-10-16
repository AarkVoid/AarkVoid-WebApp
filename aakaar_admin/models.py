from django.db import models

from profiles.models import Profile

# ********************* About Us **********************
class AboutUs_Detail(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Abouts_Topic(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    icon_label = models.CharField(max_length=50, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
# ********************* END About Us **********************

# ********************* Service **********************
class ServicePage_Detail(models.Model):
    page_tile = models.CharField(max_length=50, null=True, blank=True)
    page_head = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.page_tile

class Maintenance_Detail(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)
    legend = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Maintenance_Topic(models.Model):
    topic = models.CharField(max_length=50, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.topic

# ********************* END Service **********************

# *********************** Founders Details *******************
class Founder(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

class Founder_Details(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)
    legend = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class FounderSocialMedia(models.Model):
    social_media_name = models.CharField(max_length=50)
    link = models.URLField(max_length=200)
    enable = models.BooleanField(default=False)
    icon_label = models.CharField(max_length=50)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.social_media_name)

# *********************** END Founders Details *******************

# *********************** Testimonial *******************
class Testimonial(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    thoughts = models.TextField(null=True, blank=True)
    enable = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.thoughts

# *********************** END Testimonial *******************

# *********************** Project Request Form *******************
class ClientProjectType(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ClientWorkingType(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ProjectRequest_Form(models.Model):
    client_name = models.CharField(max_length=30)
    client_email = models.EmailField()
    client_phone_number = models.IntegerField()
    project_type = models.ForeignKey(ClientProjectType, on_delete=models.CASCADE)
    working_type = models.ForeignKey(ClientWorkingType, on_delete=models.CASCADE)
    date = models.DateField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name
