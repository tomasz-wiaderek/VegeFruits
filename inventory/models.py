from django.db import models
from user_management.models import Profile


class Unit(models.Model):
    symbol = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return self.symbol


class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    available = models.BooleanField(default=True)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock_quantity = models.IntegerField()
    min_order = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    max_order = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    pick_yourself = models.BooleanField(default=True)
    additional_desc = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f"{self.profile}'s inventory of product {self.product}"
