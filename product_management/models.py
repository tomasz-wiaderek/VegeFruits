from django.db import models

# Create your models here.


class Unit(models.Model):
    symbol = models.CharField(max_length=6)

    def __str__(self):
        return self.symbol


class Product(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.pk}: {self.name}'


class Inventory(models.Model):
    user = models.ForeignKey('user_management.User', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    available = models.BooleanField(default=True)
    pick_yourself = models.BooleanField(default=True)
    additional_desc = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    min_order = models.IntegerField()
    max_order = models.IntegerField()

    def __str__(self):
        return f'Inventory of {self.product} for user: {self.user}'
