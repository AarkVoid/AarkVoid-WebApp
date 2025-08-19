from django.db import models
from django.utils.translation import gettext_lazy as _

# ********************* Compnay Details ******************* 
class CompanyDetail(models.Model):
    companyName = models.CharField(max_length=50)
    companyEmail = models.EmailField(max_length=254)
    companyMobile = models.IntegerField()
    companyAddress = models.TextField()
    companyDescription = models.TextField()
    companyLocationUrl = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.companyName)
# ********************* END Compnay Details ******************* 
    
# ********************* Social Media ******************* 
class SocialMedia(models.Model):
    social_media_name = models.CharField(max_length=50)
    link = models.URLField(max_length=200)
    enable = models.BooleanField(default=False)
    icon_label = models.CharField(max_length=50)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.social_media_name)
# ********************* END Social Media ******************* 


class MainBannerContent(models.Model):
    small_heading = models.CharField(max_length=100, help_text="e.g., AakarDevelopers")
    main_heading = models.CharField(max_length=150, help_text="e.g., Website Development")
    description = models.TextField(help_text="e.g., Short paragraph below the heading")

    def __str__(self):
        return self.main_heading
    

class ContactSection(models.Model):
    subtitle = models.CharField(max_length=100)   # e.g., "Contact Us"
    title = models.CharField(max_length=200)      # e.g., "Drop us Message for any Query"
    description = models.TextField()              # e.g., paragraph below the heading

    def __str__(self):
        return self.title

class ContactInfoBox(models.Model):
    section = models.ForeignKey(ContactSection, related_name='info_boxes', on_delete=models.CASCADE)
    icon_class = models.CharField(max_length=100)  # e.g., "flaticon-email"
    heading = models.CharField(max_length=100)     # e.g., "Email Here"
    line1 = models.CharField(max_length=255, blank=True, null=True)  # e.g., email or address line
    line2 = models.CharField(max_length=255, blank=True, null=True)  # e.g., second line

    def __str__(self):
        return self.heading
    

class AppSection(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='app_section/')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("App Section")
        verbose_name_plural = _("App Sections")

    def __str__(self):
        return self.title

class Feature(models.Model):
    ICON_CHOICES = [
        ('flaticon-calendar', 'Calendar'),
        ('flaticon-mobile-app', 'Mobile App'),
        ('flaticon-patient', 'Patient'),
        ('flaticon-broadcasting', 'Broadcasting'),
    ]

    app_section = models.ForeignKey(AppSection, related_name='features', on_delete=models.CASCADE)
    icon = models.CharField(max_length=50, choices=ICON_CHOICES)
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = _("Feature")
        verbose_name_plural = _("Features")
        ordering = ['order']

    def __str__(self):
        return self.title