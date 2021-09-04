from django import forms
from .models import Inventory


class InventoryModelForm(forms.ModelForm):

    class Meta:
        model = Inventory
        fields = [
            'product',
            'unit',
            'stock_quantity',
            'available',
            'pick_yourself',
            'additional_desc',
            'price',
            'min_order',
            'max_order'
        ]
