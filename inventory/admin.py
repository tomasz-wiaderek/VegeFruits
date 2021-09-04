from django.contrib import admin
from .models import Inventory, Product, Unit


admin.site.register(Inventory)
admin.site.register(Product)
admin.site.register(Unit)
