from django.db import models
from inventory.models import Inventory
from django.contrib.auth.models import User


class Order(models.Model):
    statuses = [
        ('unposted', 'unposted'),
        ('unconfirmed', 'unconfirmed'),
        ('confirmed', 'confirmed'),
        ('rejected', 'rejected'),
        ('delivered', 'delivered'),
        ('cancelled', 'cancelled')
    ]
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=11, choices=statuses, default='unposted')
    with_delivery = models.BooleanField(default=False)
    add_notes = models.CharField(max_length=256, blank=True)
    created_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    predicted_delivery = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'Order no: {self.pk}'


class DeliveryLocation(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=6)
    city = models.CharField(max_length=124)
    address = models.CharField(max_length=256)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone = models.CharField(max_length=12)


class OrderLine(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
