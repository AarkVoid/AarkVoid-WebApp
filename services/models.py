from django.db import models

class Service(models.Model):
    serviceName = models.CharField(max_length=20, blank=True, null=True)
    serviceDescription = models.TextField(blank=True, null=True)
    icon = models.ImageField(upload_to='Services', blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.serviceName)

class ServiceDetail(models.Model):
    serviceName = models.ForeignKey(Service, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.serviceName)

class SubCategoryService(models.Model):
    serviceName = models.ForeignKey(Service, on_delete=models.CASCADE)
    SubCategoryName = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.serviceName)