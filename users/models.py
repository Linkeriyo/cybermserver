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

    def json(self):
        json = {
            'pk': user.pk,
            'email': self.email,
            'name': self.name,
            'surname': self.surname,
            'telephone_number': self.telephone_number,
            'address': self.address,
            'city': self.city,
            'province': self.province,
            'zip_code': self.zip_code
        }
        return json


class Computer(models.Model):
    mac_address = models.CharField(max_length=12)
    ip_address = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)

    def json(self):
        json = {
            'pk': self.pk,
            'mac_address': self.mac_address,
            'ip_address': self.ip_address,
            'alias': self.alias
        }
        return json


class CyberCafe(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=7)
    telephone_number = models.CharField(max_length=9)
    email = models.CharField(max_length=50)

    def json(self):
        json = {
            'pk': self.pk,
            'name': self.name,
            'description': self.description,
            'address': self.address,
            'city': self.city,
            'province': self.province,
            'zip_code': self.zip_code,
            'telephone_number': self.telephone_number,
            'email': self.email
        }


class ProductType(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    def json(self):
        json = {
            'pk': self.pk,
            'name': self.name,
            'description': self.description
        }
        return json


class Product(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    reference = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    
    def json(self):
        json = {
            'pk': self.pk,
            'product_type': self.product_type,
            'reference': self.reference,
            'description': self.description
        }
        return json
