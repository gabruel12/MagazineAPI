"""
URL configuration for MagazineAPI project.

"""
from django.urls import path, include

urlpatterns = [
    path("api/auth/", include("MagazineAPI.apiUsers.urls")),
    path("api/rooms/", include("RoomsAPI.urls")),
    path("api/", include("FilteringAPI.urls")),
    path("api/", include("SchedulesAPI.urls")),
]
