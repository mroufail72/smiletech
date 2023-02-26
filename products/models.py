from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import django_filters


class Type(models.Model):
    """Type Class"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    """Product Class"""
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    selected_yn = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)


class ProductList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'products_product'


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name']
