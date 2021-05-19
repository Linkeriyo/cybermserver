from django.contrib.auth.models import User
from django.db import models


class UserToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=80)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u"%s" % self.user.username


class UserExtraData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    phono = models.CharField(max_length=9)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=7)

    def json(self):
        json = {
            'pk': self.user.pk,
            'name': self.name,
            'surname': self.surname,
            'phono': self.phono,
            'address': self.address,
            'city': self.city,
            'province': self.province,
            'zip_code': self.zip_code
        }
        return json

