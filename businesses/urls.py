from django.urls import path
from . import views

urlpatterns = [
    path("check_business/", views.check_business, name="check_business"),
    path("get_businesses_by_user/", views.get_businesses_by_user, name="get_businesses_by_user"),
    path("get_posts_by_business_id/", views.get_posts_by_business_id, name="get_posts_by_business_id")
]
