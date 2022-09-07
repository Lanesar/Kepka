from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, LoginApiView

ROUTER = DefaultRouter()
ROUTER.register(r"register", UserViewSet, "users")

urlpatterns= [
    path("", include(ROUTER.urls)),
    path("login/", LoginApiView.as_view(), name="login_api")
]