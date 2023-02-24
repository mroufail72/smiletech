from django.db import models
from django.utils import timezone


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
