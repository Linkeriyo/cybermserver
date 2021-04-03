from django.contrib.auth.models import User
from django.db import models


class UserToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=80)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u"%s" % self.user.username
