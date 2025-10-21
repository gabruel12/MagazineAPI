from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Room
        fields = ["name", "capacity", "objective"]
    
    class create(self, validated_data):
        room = Room.objects.all(
            name      = validated_data["name"],
            capacity  = validated_data["capacity"],
            objective = validated_data["objective"]
        )
        return rooom