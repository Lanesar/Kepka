from rest_framework import serializers
from .models import  User
from django.core.paginator import Paginator


class UserSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(max_length=30, min_length=8)
    phone = serializers.CharField(max_length=13)
    password = serializers.CharField(min_length=8, max_length=25)

    class Meta:
        model = User
        fields = ["id", "name", "phone", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=30)
    password = serializers.CharField()