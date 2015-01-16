from django.contrib import admin

from temporary.admin import TemporaryAdmin

from .models import League


class LeagueAdmin(TemporaryAdmin):
    pass

admin.site.register(League, LeagueAdmin)
