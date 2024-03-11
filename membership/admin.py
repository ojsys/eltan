from django.contrib import admin

from .models import Conference, ConferenceRegistration

# Register your models here.

admin.site.register(Conference)
admin.site.register(ConferenceRegistration)