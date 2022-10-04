import django_filters
from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, viewsets
from rest_framework.viewsets import ModelViewSet
from .pagination import PaginateProduct, StockPagination, BestsellersPagination
from .models import  *
from .serializers import *



class SlidersListView(generics.ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer



class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ('title', 'description', 'min_price', 'max_price')


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'description']
    filter_class = ProductFilter
    pagination_class = PaginateProduct


class MessengerViewSet(generics.ListCreateAPIView):
    serializer_class = MessengerSerializer
    queryset = Messenger.objects.all()


class BestsellerViewSet(generics.ListCreateAPIView):
    serializers_class = BestsellerSerializers
    queryset = Product.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'description']
    filter_class = ProductFilter
    pagination_class = PaginateProduct


class StockViewSet(generics.ListCreateAPIView):
    serializer_class = SliderSerializer
    queryset = Product.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['title']
    filter_class = ProductFilter
    pagination_class = PaginateProduct


class GetCartProductViewSet(ModelViewSet):
    serializer_class = GetCartProductSerializer
    queryset = CartProduct.objects.all()


class CartProductViewSet(ModelViewSet):
    serializer_class = CartProductSerializer
    queryset = CartProduct.objects.all()


class CartViewSet(ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()








