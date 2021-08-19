from django import forms

from .models import User, UserLocation


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'type'
        ]


class UserLocationModelForm(forms.ModelForm):

    zip_code = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'e.g.: 00-400'
    }))
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Your city'
    }))
    address = forms.CharField(max_length=250, widget=forms.TextInput(attrs={
        'placeholder': 'Your street and no.'
    }))

    class Meta:
        model = UserLocation
        fields = [
            'zip_code',
            'voivodship',
            'district',
            'city',
            'address'
        ]
