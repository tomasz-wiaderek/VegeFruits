from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image


class ProfileType(models.Model):
    types = [
             ('producer', 'Producer'),
             ('customer', 'Customer')
    ]
    type = models.CharField(max_length=8, choices=types)

    def __str__(self):
        return self.type


class Profile(models.Model):
    types = [
             ('producer', 'Producer'),
             ('customer', 'Customer')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    profile_type = models.CharField(max_length=8, choices=types, default='customer')

    def __str__(self):
        return f"{self.user.username}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class ProfileAdditionalInfo(models.Model):
    phone = models.CharField(max_length=12)
    additional_desc = models.TextField(blank=True)
    delivery_available = models.BooleanField(default=False)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('user_man:profile')


class Voivodship(models.Model):
    name = models.CharField(max_length=18)

    def __str__(self):
        return f'{self.name}'


class District(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


class ProfileLocation(models.Model):
    zip_code = models.CharField(max_length=6)
    voivodship = models.ForeignKey(Voivodship, on_delete=models.PROTECT)
    district = models.ForeignKey(District, on_delete=models.PROTECT)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.zip_code} {self.city}, {self.address}'

    def get_absolute_url(self):
        return reverse('user_man:profile')
