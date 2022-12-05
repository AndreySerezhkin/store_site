from django.db import models

from oauth.models import AuthUser

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']


class ProductStatus(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, verbose_name='Описание')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата созщдания')
    photo = models.ImageField(upload_to='photos/product/%Y/%m/%d/', blank=True)
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    status = models.ForeignKey(ProductStatus, on_delete=models.PROTECT, related_name='products')
    seller = models.ForeignKey(AuthUser, on_delete=models.PROTECT, related_name='products')

    def __str__(self) -> str:
        return self.name
    