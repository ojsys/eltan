from django.contrib import admin

from .models import Conference, ConferenceRegistration, MemberProfile, MembershipType

# Register your models here.
admin.site.register(MemberProfile)
admin.site.register(Conference)
admin.site.register(ConferenceRegistration)