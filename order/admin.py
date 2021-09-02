from django.contrib import admin
from .models import Order, OrderLine, DeliveryLocation

admin.site.register(Order)
admin.site.register(OrderLine)
admin.site.register(DeliveryLocation)
