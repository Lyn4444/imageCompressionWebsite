from django.db import models


# Create your models here.
class Login(models.Model):
    IsDelect_choices = {
        (0, "登记"),
        (1, "注销")
    }

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    pwd = models.CharField(max_length=255)
    salt = models.CharField(max_length=255)
    isDelect = models.BooleanField(choices=IsDelect_choices)
    datetime = models.TimeField()

    class Mate:
        permissions = ()

