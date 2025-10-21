from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import DestroyAPIView
from rest_framework.views import APIView

from .serializers import SchedulesSerializers
from .models import Schedules

class CreateScheduleView(APIView):
    def post(self, request):
        serializer = SchedulesSerializers(data=request.data)
        if serializer.is_valid():
            schedule = serializer.save(created_by=request.user)
            return Response({"success": "The schedules has created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteScheduleView(DestroyAPIView):
    queryset = Schedules.objects.all()
    serializer_class = SchedulesSerializers
    lookup_field = 'id'