from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from django.contrib.auth.models import User

from .serializers import RoomSerializer
from .models import Room

class CreateRoomView(APIView):
    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            room = serializer.save()
            return Response({"success": "The room was created."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteRoomView(DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = 'id'

class EditRoomView(UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = 'id'