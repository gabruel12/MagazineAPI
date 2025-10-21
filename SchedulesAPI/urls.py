from django.urls import path

from .views import CreateScheduleView, DeleteScheduleView

urlpatterns = [
    path('create/', CreateScheduleView.as_view(), name="create-schedule"),
    path('remove/<int:id>/', DeleteScheduleView.as_view(), name="delete-schedule"),
]