from django.contrib import admin
from .models import DeliveryLocation, Order, OrderLine

# Register your models here.

admin.site.register(Order)
admin.site.register(OrderLine)
admin.site.register(DeliveryLocation)
