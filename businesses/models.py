from django.db.models.deletion import CASCADE
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
        editable=False,
        unique=True,
        default=create_new_business_id
    )
            
    def json(self):
        return {
            "pk": self.pk,
            "name": self.name,
            "description": self.description,
            "address": self.address,
            "city": self.city,
            "province": self.province,
            "zip_code": self.zip_code,
            "phono": self.phono,
            "email": self.email,
            "image": self.image,
            "business_id": self.business_id
        }
        

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=5000)
    image = models.CharField(max_length=200)
    date = models.CharField(max_length=11)
    business = models.ForeignKey(CyberCafe, CASCADE)
    
    def json(self):
        return {
            "pk": self.pk,
            "title": self.title,
            "content": self.content,
            "image": self.image,
            "date": self.date
        }
        
        
class Computer(models.Model):
    mac_address = models.CharField(max_length=12)
    ip_address = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)
    business = models.ForeignKey(CyberCafe, CASCADE)

    def json(self):
        json = {
            "pk": self.pk,
            "mac_address": self.mac_address,
            "ip_address": self.ip_address,
            "alias": self.alias,
            "business_id": self.business.business_id
        }
        return json

