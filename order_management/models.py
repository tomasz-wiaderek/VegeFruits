from django.db import models

# Create your models here.


from django.contrib.auth import get_user_model


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class DeliveryLocation(models.Model):
    zip_code = models.CharField(max_length=6)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=12)
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
    # producer = models.ForeignKey('user_management.User', related_name='producer', on_delete=models.SET(get_sentinel_user))
    # customer = models.ForeignKey('user_management.User', related_name='customer', on_delete=models.SET(get_sentinel_user))
    delivery = models.BooleanField(default=False)
    predicted_delivery_date = models.DateField()
    additional_notes = models.CharField(max_length=300)
    delivery_location = models.ForeignKey(DeliveryLocation, on_delete=models.SET_DEFAULT, default='Not specified')


class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey('product_management.Product', on_delete=models.CASCADE)
    unit = models.CharField(max_length=6)  # unit from Inventory
    quantity = models.DecimalField(max_digits=5, decimal_places=2)  # quantity from user input
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)  # price imported from Inventory
    price = models.DecimalField(max_digits=6, decimal_places=2)  # price calculated
