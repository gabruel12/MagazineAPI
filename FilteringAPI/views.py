from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from RoomsAPI.models import Room
from RoomsAPI.serializers import RoomSerializer
from SchedulesAPI.models import Schedules
from SchedulesAPI.serializers import SchedulesSerializers

MODEL_SERIALIZER_MAP = {
    'rooms': (Room, RoomSerializer),
    'schedules': (Schedules, SchedulesSerializers),
}

class DbListAPI(APIView):
    def get(self, request, dbname):
        model_info = MODEL_SERIALIZER_MAP.get(dbname)
        if not model_info:
            return Response({"detail": "Table not found."}, status=status.HTTP_404_NOT_FOUND)
        model, serializer_class = model_info
        queryset = model.objects.all()
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)

class FIlterAPI(APIView):
    def get(self, request, dbname, objname):
        model_info = MODEL_SERIALIZER_MAP.get(dbname)
        if not model_info:
            return Response({"detail": "Table not found."}, status=status.HTTP_404_NOT_FOUND)
        model, serializer_class = model_info
        try:
            obj = model.objects.get(name=objname)
        except model.DoesNotExists:
            return Response({"detail": "Object not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializer_class(obj)
        return Response(serializer.data)
