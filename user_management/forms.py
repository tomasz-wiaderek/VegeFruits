from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from .models import UserLocation


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
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
