from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("check_user_extra_data/", views.check_user_extra_data, name="check_user_extra_data"),
    path("set_user_extra_data/", views.set_user_extra_data, name="set_user_extra_data")
]
