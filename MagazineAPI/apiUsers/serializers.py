from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class CadasterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model  = User
        fields = ["username", "email", "password"]
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data["username"],
            email    = validated_data.get('email'),
            password = validated_data["password"]
        )
        return user
    
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        user = authenticate(username=data.get("username"), password=data.get("password"))
        if user and user.is_active:
            data["user"] = user
            return data
        raise serializers.ValidationError("Credenciais inválidas.")