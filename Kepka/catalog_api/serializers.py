from rest_framework import serializers

from .models import *


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class BestsellerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'bestseller', 'price', 'image')


class StockSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'old_price', 'price')


class ProductForCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'image', 'color')


class GetCartProductSerializer(serializers.ModelSerializer):
    product = ProductForCartSerializer()

    class Meta:
        model = CartProduct
        fields = ('id', 'product', 'amount', 'final_price')


class CartProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartProduct
        fields = ('id', 'product', 'amount', 'final_price')


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class MessengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messenger
        fields = '__all__'


