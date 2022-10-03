import os

from django.db import models

# Create your models here.


class Brand(models.Model):
    name = models.CharField("Бренд", max_length=50)
    icon = models.FileField("Иконка бренда", upload_to='brand_icon/')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
         return self.name

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"





class Sizes(models.Model):
    cap_sizes= models.CharField("Размеры шапки", max_length=2)

    def __str__(self):
        return f'{self.cap_sizes}'

    class Meta:
        verbose_name = "Размер"
        verbose_name_plural = "Размеры"

class Caps(models.Model):
    brand = models.ForeignKey(Brand, verbose_name="Имя бренда", on_delete=models.CASCADE, null=True)
    name = models.CharField("Названия", max_length=200)
    price = models.IntegerField("цена")
    size = models.ManyToManyField(Sizes, verbose_name="Размер", related_name='sizes')
    color=models.CharField("Цвет",max_length=70)
    description = models.TextField("Описания")
    is_available = models.BooleanField(default=True, verbose_name="в Наличии")
    discount_price=models.IntegerField(null=True, blank=True)
    is_bestseller=models.TextField(default=True,verbose_name="самые продаваемые",max_length=180)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Кепка"
        verbose_name_plural = "Кепки"


