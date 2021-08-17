from django import forms

from .models import User, UserLocation


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'type',
            'additional_info'
        ]


class UserLocationModelForm(forms.ModelForm):
    class Meta:
        model = UserLocation
        fields = [
            'zip_code',
            'voivodship',
            'district',
            'city',
            'address',
            'user'
        ]
