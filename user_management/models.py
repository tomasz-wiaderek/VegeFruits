from django.db import models


# Create your models here.


class UserType(models.Model):
    type = models.CharField(max_length=8, null=False, choices=[('admin', 'admin'),
                                                               ('producer', 'producer'),
                                                               ('customer', 'customer')])

    def __str__(self):
        return f'{self.pk}: {self.type}'


class UserAdditionalInfo(models.Model):
    phone = models.CharField(max_length=12)
    additional_desc = models.TextField(null=True)
    delivery_available = models.BooleanField(default=False)


class User(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=320)
    type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    additional_info = models.ForeignKey(UserAdditionalInfo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk}: {self.type} {self.name}'


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
    voivodship = models.ForeignKey(Voivodship, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Location of user: {self.user}'
