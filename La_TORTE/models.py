from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Категории"""
    name = models.CharField('Категория', max_length=150)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=160, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('filter_prod', kwargs={'cat_slug': self.url})


class Product(models.Model):
    """Продукция"""
    image = models.ImageField('Изображение', upload_to='image/')
    name = models.CharField('Название', max_length=150)
    price = models.PositiveSmallIntegerField('Цена')
    description = models.TextField('Описание')
    weight = models.PositiveSmallIntegerField('Вес', default=1000)
    url = models.SlugField(max_length=150, unique=True)
    popular = models.BooleanField('Популярные', default=False)
    draft = models.BooleanField('Черновик', default=False)
    category = models.ForeignKey(
        Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name = 'Продукция'
        verbose_name_plural = 'Продукция'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_prod', kwargs={'slug': self.url})


class ProductDetail(models.Model):
    """Изображения продукции"""
    image_detail = models.ImageField('Изображение', upload_to='image_products/')
    product = models.ForeignKey(Product, verbose_name='Продукция', on_delete=models.CASCADE,)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'




