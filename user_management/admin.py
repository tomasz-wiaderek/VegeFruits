from django.contrib import admin
from .models import Profile, ProfileType, ProfileLocation, ProfileAdditionalInfo, Voivodship, District

admin.site.register(Profile)
admin.site.register(ProfileType)
admin.site.register(ProfileLocation)
admin.site.register(ProfileAdditionalInfo)
admin.site.register(Voivodship)
admin.site.register(District)
