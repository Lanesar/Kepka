
# Create your views here.

from .serializers import  UserRegisterSerializer
from .models import User
from rest_framework.permissions import AllowAny

from rest_framework import generics



class RegisterApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [
        AllowAny,
    ]





# Create your views here.

# Create your views here.
