from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password


class UserRegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=35)
    phone = serializers.CharField(max_length=13)
    password = serializers.CharField(
        validators=[validate_password], write_only=True, required=True
    )
    password2 = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = User
        fields = ["name", "phone", "password", "password2"]

    def validate(self, attrs):
        if attrs["password2"] != attrs["password"]:
            raise serializers.ValidationError("Passwords didnt match!")
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(
            name=validated_data["name"],
            phone=validated_data["phone"],
            password=validated_data["password"],
        )


