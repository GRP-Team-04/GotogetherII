# Django Library. Modified by Grp group 4
from django.contrib import admin

# Register your models here.

from team_sports_app.models import Event, Participant

admin.site.register(Event)
admin.site.register(Participant)
