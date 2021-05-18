from django.db import models

# Create your models here.
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