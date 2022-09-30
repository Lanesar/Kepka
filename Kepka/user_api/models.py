from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Создайте свои модели здесь.


class UserManager(BaseUserManager):
    def _createuser(self, name, phone, password, **extra_fields):
        if not name:
            raise ValueError("Введи name")
        user = self.model(name=name, phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, name, phone, password):
        return self._createuser(name, phone, password)

    def create_superuser(self, name, phone, password):
        return self._createuser(name, phone, password, is_staff=True, is_superuser=True)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=30)
    photo = models.ImageField(
        default="media/avatar.jpg", upload_to="media/upload_to_user_media"
    )
    phone = PhoneNumberField(unique=True, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["name"]

    objects = UserManager()

    def __str__(self):
        return f"{self.name} with {self.phone}"


# Create your models here.
