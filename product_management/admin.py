from django.contrib import admin
from .models import Unit, Product, Inventory

# Register your models here.

admin.site.register(Unit)
admin.site.register(Product)
admin.site.register(Inventory)
