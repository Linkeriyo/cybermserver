from annoying.functions import get_object_or_None
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here. 

class CreditCard(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    card_holder = models.CharField(max_length=40)
    card_number = models.CharField(max_length=16)
    expires_month = models.IntegerField()
    expires_year = models.IntegerField()
    cvv = models.CharField(max_length=4)
    
    def json(self):
        return {
            "pk": self.pk,
            "card_holder": self.card_holder,
            "card_number": self.card_number,
            "expires_month": self.expires_month,
            "expires_year": self.expires_year,
            "cvv": self.cvv
        }
    
