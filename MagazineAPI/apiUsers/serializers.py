from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class CadasterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data["username"],
            email    = validated_data.get('email'),
            password = validated_data["password"]
        )
        return user
    
class LoginUserSerializer(serializers.Serializer):
    class Meta:
        username = serializers.CharField()
        password = serializers.CharField(write_only=True)
    
    def validation(self, data):
        user = authenticate(**data)
        if user and user.is_active():
            return user
        raise serializers.ValidationError("Credenciais inválidas.")