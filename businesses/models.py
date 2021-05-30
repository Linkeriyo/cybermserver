from businesses.utils import create_new_business_id
from django.db import models

# Create your models here.
class CyberCafe(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=7)
    phono = models.CharField(max_length=9)
    email = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    business_id = models.CharField(
        max_length=10,
        blank=True,
        editable=True,
        unique=True,
        default=create_new_business_id
    )
            
    def json(self):
        json = {
            'pk': self.pk,
            'name': self.name,
            'description': self.description,
            'address': self.address,
            'city': self.city,
            'province': self.province,
            'zip_code': self.zip_code,
            'phono': self.phono,
            'email': self.email,
            'image': self.image,
            'business_id': self.business_id
        }
        return json