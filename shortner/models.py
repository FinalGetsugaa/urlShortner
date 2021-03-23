from django.db import models


# Create your models here.
class Url(models.Model):
    link = models.CharField(default='', max_length=10000)
    uuid = models.CharField(default='', max_length=10)
