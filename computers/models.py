import builtins
from django.db import models
from django.db.models.deletion import CASCADE
from businesses.models import CyberCafe

# Create your models here.
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