from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    salt = models.CharField(max_length=255)
    passwd = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    isdelete = models.BooleanField(default=False)
    avatar = models.CharField(max_length=255)
