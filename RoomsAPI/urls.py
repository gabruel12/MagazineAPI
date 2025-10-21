from django.urls import path
from .views import CreateRoomView, EditRoomView, DeleteRoomView

urlpatterns = [
    path('create/', CreateRoomView.as_view(), name="createRoom"),
    path('edit/<int:id>/', EditRoomView.as_view(), name="editRoom"),
    path('delete/<int:id>/', DeleteRoomView.as_view(), name="deleteRoom"),
]