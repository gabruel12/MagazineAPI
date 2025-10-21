"""
URL configuration for MagazineAPI project.

"""
from django.urls import path, include

urlpatterns = [
    path("api/auth/", include("MagazineAPI.apiUsers.urls"))
]
