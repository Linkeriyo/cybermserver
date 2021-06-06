from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.
class PaymentMethodType(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    

class PaymentMethod(models.Model):
    method_type = models.ForeignKey(PaymentMethodType, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)
    
    
class CreditCard(models.Model):
    payment_method = models.ForeignKey(PaymentMethod, on_delete=CASCADE)
    card_holder = models.CharField(max_length=40)
    card_number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=4)
    
