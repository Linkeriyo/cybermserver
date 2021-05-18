from django.db import models

# Create your models here.
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
        return json