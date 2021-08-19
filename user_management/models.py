from django.db import models
from django.urls import reverse

# Create your models here.


class UserType(models.Model):
    types = [('admin', 'Admin'),
             ('producer', 'Producer'),
             ('customer', 'Customer')]
    type = models.CharField(max_length=8, choices=types)

    def __str__(self):
        return self.type


class UserAdditionalInfo(models.Model):
    phone = models.CharField(max_length=12)
    additional_desc = models.TextField(blank=True)
    delivery_available = models.BooleanField(default=False)

    def __str__(self):
        user = User.objects.get(additional_info=self.pk)
        return f'Addition info for {user}'


class User(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=320)
    type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    additional_info = models.ForeignKey(UserAdditionalInfo, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.pk}: {self.type} {self.name}'

    def get_absolute_url(self):
        return reverse('user_man:user-detail', kwargs={'pk': self.pk})


class Voivodship(models.Model):
    name = models.CharField(max_length=18)

    def __str__(self):
        return f'{self.name}'


class District(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


class UserLocation(models.Model):
    zip_code = models.CharField(max_length=6)
    voivodship = models.ForeignKey(Voivodship, on_delete=models.SET_DEFAULT, default='Not chosen')
    district = models.ForeignKey(District, on_delete=models.SET_DEFAULT, default='Not chosen')
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return f'{self.zip_code} {self.city} {self.address}'
