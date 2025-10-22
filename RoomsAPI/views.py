from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

from .serializers import RoomSerializer
from .models import Room
from Logs.models import logger

class CreateRoomView(APIView):
    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            room = serializer.save()
            logger('success_room_create', none_room=room.name)
            return Response({"success": "The room was created."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteRoomView(DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        room_id = instance.id

        logger('success_room_delete', none_id=room_id)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class EditRoomView(UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            response = super().update(request, *args, **kwargs)
            room_id = instance.id

            logger("success_room_edited", none_id=room_id)
            return response
        except ValidationError as e:
            room_id = instance.id
            logger("failed_room_edit", none_id=room_id)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)