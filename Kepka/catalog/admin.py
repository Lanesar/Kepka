from django.contrib import admin
from .models import Product, Brand

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'original_price', 'discount_price','is_best_seller', 'created_at', 'updated_at')

