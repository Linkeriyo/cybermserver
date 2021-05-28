from django.urls import path
from . import views

urlpatterns = [
    path("check_business/", views.check_business, name="check_business")
]
