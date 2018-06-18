from django.db import models

# Create your models here.
class Device(models.Model):
    email = models.EmailField(null=True)
    email_verified = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=50, null=True)
    display_name = models.CharField(max_length=20, null=True)
    photo_url = models.CharField(max_length=250, null=True)
    disabled = models.BooleanField(default=False)
    uuid = models.CharField(max_length=250, null=True)
