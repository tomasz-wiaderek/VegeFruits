from django.contrib import admin
from .models import Profile, ProfileLocation, ProfileAdditionalInfo, Voivodship, District

admin.site.register(Profile)
admin.site.register(ProfileLocation)
admin.site.register(ProfileAdditionalInfo)
admin.site.register(Voivodship)
admin.site.register(District)
