from django.contrib import admin
from .models import *


admin.site.register(Slider)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Brand)
admin.site.register(Size)


# class ProductObjectsAdmin(admin.StackedInline):
#
#     model = Product
#     max_num = 8
#
#
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#
#     inlines = [ProductObjectsAdmin]
#     list_display = ('title', 'article', 'size_line', 'quantity_in_line',
#                     'collection')
#     search_fields = ('title', 'article',)
#
#
# class CartObjectsAdmin(admin.StackedInline):
#
#     model = Cart
#     max_num = 8
#
#
# @admin.register(Cart)
# class CartAdmin(admin.ModelAdmin):
#
#     inlines = [CartObjectsAdmin]
#     list_display = ('products', 'quantity', 'size', 'max_price',
#                     )
#     search_fields = ('products', 'max_price',)
#
#
# class CartProductObjectsAdmin(admin.StackedInline):
#
#     model = CartProduct
#     max_num = 8
#
#
# @admin.register(CartProduct)
# class ProductAdmin(admin.ModelAdmin):
#
#     inlines = [CartProductObjectsAdmin]
#     list_display = ('amount', 'product')
#     search_fields = ('amount', 'product')


