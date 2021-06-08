from django.urls import path
from . import views

urlpatterns = [
    path("get_methods_by_user/", views.get_methods_by_user, name="get_methods_by_user"),
    path("register_new_card/",views.register_new_card, name="register_new_card"),
    path("remove_card/", views.remove_card, name="remove_card"),
    path("get_cybergold/", views.get_cybergold, name="get_cybergold")
]
