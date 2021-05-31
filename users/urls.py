from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("check_user_extra_data/", views.check_user_extra_data, name="check_user_extra_data"),
    path("set_user_extra_data/", views.set_user_extra_data, name="set_user_extra_data"),
    path("add_cybercafe_to_user/", views.add_cybercafe_to_user, name="add_cybercafe_to_user"),
    path("remove_cybercafe_from_user/", views.remove_cybercafe_from_user, name="remove_cybercafe_from_user")
]
