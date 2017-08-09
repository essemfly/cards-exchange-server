from django.db import models


# Create your models here.


class Dogs(models.Model):
    name = models.CharField(max_length=100, null=True)
    pic_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
