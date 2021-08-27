from django.db import models
from django.conf import settings
from inventory.models import Inventory


class Order(models.Model):
    statuses = [
        ('unp', 'unposted'),
        ('unc', 'unconfirmed'),
        ('con', 'confirmed'),
        ('rej', 'rejected'),
        ('del', 'delivered'),
        ('can', 'cancelled')
    ]
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=statuses, default='unposted')
    with_delivery = models.BooleanField(default=False)
    add_notes = models.CharField(max_length=250, blank=True)
    created_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    predicted_delivery = models.DateField()


class DeliveryLocation(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=6)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=12)


class OrderLine(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=8, decimal_places=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
