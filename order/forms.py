from django import forms
from .models import OrderLine


class OrderLineForm(forms.ModelForm):

    class Meta:
        model = OrderLine
        fields = [
            'inventory',
            'quantity'
        ]
