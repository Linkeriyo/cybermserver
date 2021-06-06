from payments.models import PaymentMethod, PaymentMethodType
from django.contrib import admin

# Register your models here.
admin.site.register(PaymentMethodType)
admin.site.register(PaymentMethod)