from rest_framework.viewsets import ModelViewSet

from .serializers import CartSerializer
from .models import Cart


class CartViewSet(ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()