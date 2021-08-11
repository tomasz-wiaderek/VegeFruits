from django.contrib import admin
from .models import User, UserType, UserLocation, UserAdditionalInfo, District, Voivodship

# Register your models here.

admin.site.register(UserType)
admin.site.register(UserAdditionalInfo)
admin.site.register(UserLocation)
admin.site.register(User)
admin.site.register(District)
admin.site.register(Voivodship)
