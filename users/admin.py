from django.contrib import admin
from users.models import *

# Register your models here.
admin.site.register(UserToken)
admin.site.register(UserExtraData)
admin.site.register(UserCybercafes)