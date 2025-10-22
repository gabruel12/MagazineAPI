from django.urls import path
from .views import FilterAPI, DbListAPI

urlpatterns = [
    path('filter/<str:dbname>/<str:objname>/', FilterAPI.as_view(), name="filter"),
    path('list/<str:dbname>/', DbListAPI.as_view(), name="list"),
]