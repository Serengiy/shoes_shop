from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=40)
    image = models.ImageField(verbose_name='Фото', upload_to='static/images/categories', null=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название товара', unique=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(verbose_name='Цена')
    description = models.CharField(max_length=150, null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(verbose_name='Фото', upload_to='static/images/products', null=True)
    is_discount = models.BooleanField(verbose_name='Акция', null=True, blank=True)
    is_new = models.BooleanField(verbose_name='Новинка', null=True, blank=True)

    def __str__(self):
        return self.name
