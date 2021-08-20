from django.contrib import admin
from .models import Profile, UserType, UserLocation, UserAdditionalInfo, Voivodship, District

admin.site.register(Profile)
admin.site.register(UserType)
admin.site.register(UserLocation)
admin.site.register(UserAdditionalInfo)
admin.site.register(Voivodship)
admin.site.register(District)
