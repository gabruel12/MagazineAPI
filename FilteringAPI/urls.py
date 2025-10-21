from django.urls import path
from .views import FIlterAPI, DbListAPI

urlpatterns = [
    path('filter/<str:dbname>/<str:objname>/', FIlterAPI.as_view(), name="filter"),
    path('list/<str:dbname>/', DbListAPI.as_view(), name="list"),
]