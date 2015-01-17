from django.contrib import admin

class TemporaryAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'user', 'session_key', 'ip_address', 'pub_date']
