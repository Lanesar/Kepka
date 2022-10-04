from django.db import models
from django.core.exceptions import ValidationError
from colorfield.fields import ColorField
from ckeditor.fields import RichTextField
import json


class Messenger(models.Model):
    whatsapp = models.CharField(max_length=255, verbose_name='ССылка на whatsapp')
    telegram = models.CharField(max_length=255, verbose_name='ССылка на telegram')

    def save(self, *args, **kwargs):
        """ generate link """
        if len(self.telegram) and len(self.whatsapp) <= 15:  # check telegram link created already
            self.telegram = f'https://t.me/{self.telegram}/'
            self.whatsapp = f'https://wa.me/{self.whatsapp}'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Соц. сети'
        verbose_name_plural = 'Соц. сети'


class Slider(models.Model):
    """ слайдер на главной странице """
    image = models.ImageField(upload_to='slider/%Y/%m/%d')
    link = models.URLField(verbose_name='ссылка', blank=True )

    def __str__(self):
        return f"link : {self.image}"

    class Meta:
        verbose_name = 'Слайдер. Главная страница'
        verbose_name_plural = 'Слайдер. Главная страница'




class Size(models.Model):
    """ размер продукта """
    size = models.CharField(max_length=100, verbose_name='размер')

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размер'



class Product(models.Model):

    image = models.ImageField(upload_to='product/%Y/%m/%d', verbose_name='Изображение', blank=True)
    size = models.ForeignKey('Size', verbose_name='размер', blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    article = models.SlugField(unique=True, verbose_name='Артикул товара')
    likes = models.IntegerField(verbose_name='лайки', default=0)

    description = RichTextField(verbose_name='Описание', null=True)
    number = models.IntegerField(verbose_name='количество в линейке')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена', blank=True)
    discount = models.DecimalField(max_digits=100, decimal_places=2, blank=True, verbose_name="cкидка")
    old_price = models.DecimalField(max_digits=9, decimal_places=2,verbose_name='Неактуальная цена',)

    bestseller = models.BooleanField(default=False,verbose_name='Бестселлер')
    novelty = models.BooleanField(default=False,verbose_name='новинки')
    color = ColorField(verbose_name='Цвет товара')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """ калькуляуия """
        if self.discount != 0:
            self.price = self.old_price - ((self.old_price * self.discount) / 100)
        else:
            self.price = self.old_price
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'




class Brand(models.Model):
    brand = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    image = models.ImageField(upload_to='brand/%Y/%m/%d', verbose_name='Бренд', blank=True)
    title = models.CharField(max_length=255, verbose_name='Имя-бренда')


class Cart(models.Model):

    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=255)
    max_price = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


    def __str__(self):
        return f"{self.products}  |  {self.max_price}"



class CartProduct(models.Model):
    """ Корзина """

    amount = models.PositiveIntegerField(default=1, verbose_name='Количество товара')
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    lines = models.IntegerField(verbose_name='Линейка')
    discount = models.DecimalField(max_digits=100,decimal_places=2,blank=True)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')


    def __str__(self):
        return "Продукт: {} (для корзины)".format(self.product.title)



    def save(self, *args, **kwargs):
        """  калькуляция """
        if self.product.price is None and self.discount is None:
            self.discount = 0
        else:
            self.discount = self.product.old_price - self.product.price
        self.final_price = self.amount * self.product.old_price
        self.lines = self.product.number
        super().save(*args, **kwargs)


















