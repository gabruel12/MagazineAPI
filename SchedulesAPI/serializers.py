from rest_framework import serializers

from .models import Schedules

class SchedulesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Schedules
        fields = '__all__'
        read_only_files = ['created_by']
    
    def validate(self, data):
        start = data.get('start_time')
        end = data.get('end_time')
        room = data.get('room')

        if end <= start:
            raise serializers.ValidationError("End time must be after start time.")

        conflicts = Schedules.objects.filter(
            room           = room,
            start_time__lt = start,
            end_time__gt   = end
        )

        if self.instance:
            conflicts = conflicts.exclude(pk=self.instance.pk)
        if conflicts.exists():
            raise serializers.ValidationError("Time conflict: the room is already reserved in this range.")
        return data