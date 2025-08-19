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
    comments = models.CharField(max_length=50, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name

# *********************** END Project Request Form *******************


# ****************** Projects Table ****************
class Project(models.Model):
    title = models.CharField(max_length=30)
    project_code = models.CharField(max_length=300)
    project_type = models.ForeignKey(ClientProjectType, on_delete=models.CASCADE)
    working_type = models.ForeignKey(ClientWorkingType, on_delete=models.CASCADE)
    project_date = models.DateField()
    discreption = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class projectPage(models.Model):
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=100)
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.title
    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='blog/')
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class BlogDetails(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class PricingPlan(models.Model):
    PLAN_ICON_CHOICES = [
        ("fas fa-paper-plane", "Paper Plane"),
        ("fas fa-gem", "Gem"),
        ("fas fa-rocket", "Rocket"),
    ]

    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    icon_class = models.CharField(max_length=50, choices=PLAN_ICON_CHOICES)
    view_link = models.URLField(default="#", help_text="Link to detail or purchase page")

    def __str__(self):
        return self.title


class PlanFeature(models.Model):
    plan = models.ForeignKey(PricingPlan, related_name='features', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    is_included = models.BooleanField(default=True)  # True for 'true', False for 'false'

    def __str__(self):
        return f"{self.description} ({'Included' if self.is_included else 'Not Included'})"