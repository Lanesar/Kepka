from django.db import models
from django.contrib.auth import get_user_model

from catalog.models import Product

User = get_user_model()


class FavoriteProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
