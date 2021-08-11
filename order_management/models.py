from django.db import models

# Create your models here.


class DeliveryLocation(models.Model):
    zip_code = models.CharField(max_length=6)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)


class Order(models.Model):
    statuses = [
        ('unposted', 'unposted'),
        ('unconfirmed', 'unconfirmed'),
        ('confirmed', 'confirmed'),
        ('rejected', 'rejected'),
        ('delivered', 'delivered'),
        ('cancelled', 'cancelled'),
    ]
    order_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    status = models.CharField(max_length=11, choices=statuses)
    producer = models.ForeignKey('user_management.User', on_delete=models.CASCADE)
    customer = models.ForeignKey('user_management.User', on_delete=models.CASCADE)
    delivery = models.BooleanField(default=False)
    predicted_delivery_date = models.DateField()
    additional_notes = models.CharField(max_length=300)
    delivery_location = models.ForeignKey(DeliveryLocation, on_delete=models.CASCADE)


class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey('product_management.Product', on_delete=models.CASCADE)
    unit = models.ForeignKey('product_management.Unit', on_delete=models.SET('None'))
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
