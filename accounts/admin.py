from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.admin.sites import NotRegistered
from django.contrib.auth.admin import UserAdmin

try:
    admin.site.unregister(get_user_model())
except NotRegistered:
    pass
admin.site.register(get_user_model(), UserAdmin)
