from django.db import models

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