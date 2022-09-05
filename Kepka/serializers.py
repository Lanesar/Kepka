from.models import*
from rest_framework import serializers


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = 'name icon'.split()



class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = 'id name icon'.split()



class SizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sizes
        fields = 'cap_sizes'.split()



class CapsSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    size = SizesSerializer(read_only=True, many=True)

    class Meta:
        model = Caps
        fields = 'id brand name price size description is_available discount_price  caps image'.split()



