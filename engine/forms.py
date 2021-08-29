from django import forms
from user_management.models import Voivodship, District


class SearchForm(forms.Form):
    product_name = forms.CharField(max_length=250, required=False)
    producer_name = forms.CharField(max_length=250, required=False)
    voivodship = forms.ModelChoiceField(Voivodship.objects.all(), empty_label='Search all', required=False)
    district = forms.ModelChoiceField(District.objects.all(), empty_label='Search all', required=False)
    city = forms.CharField(max_length=100, required=False)
    delivery_available = forms.BooleanField(required=False)

