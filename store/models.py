from django.db import models

# Create your models here.
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
