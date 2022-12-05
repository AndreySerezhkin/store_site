from django.contrib import admin
from .models import *

class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name','email', 'registered_at')
    list_display_link = ('full_name')

admin.site.register(AuthUser, AuthUserAdmin)