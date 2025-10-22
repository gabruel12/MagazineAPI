from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import DestroyAPIView
from rest_framework.views import APIView

from .serializers import SchedulesSerializers
from .models import Schedules
from Logs.models import logger

class CreateScheduleView(APIView):
    def post(self, request):
        serializer = SchedulesSerializers(data=request.data)
        if serializer.is_valid():
            schedule = serializer.save(created_by=request.user)
            logger("success_schedule_create", none_name=schedule)
            return Response({"success": "The schedules has created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteScheduleView(DestroyAPIView):
    queryset = Schedules.objects.all()
    serializer_class = SchedulesSerializers
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        schedule_id = instance.id

        logger('success_schedule_delete', none_id=schedule_id)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

