from django.urls import path
from .views import LoginView, CadasterView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('cadaster/', CadasterView.as_view(), name="cadaster"),
    path('logout/', LogoutView.as_view(), name="logout"),
]