from django.contrib.auth.models import User
from django.db import models


class UserToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=80)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u"%s" % self.user.username


class UserExtraData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    telephone_number = models.CharField(max_length=9)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=7)


class Computer(models.Model):
    mac_address = models.CharField(max_length=12)
    ip_address = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)


class CyberCafe(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=7)
    telephone_number = models.CharField(max_length=9)
    email = models.CharField(max_length=50)

