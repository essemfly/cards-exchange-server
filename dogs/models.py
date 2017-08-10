from django.db import models


# Create your models here.

class DogsImage(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    datafile = models.FileField()
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=1000, null=True)
