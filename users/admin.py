from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group

admin.site.register(CustomUserStatus)
admin.site.register(CustomUsers)
admin.site.register(CustomUserGroup)
admin.site.unregister(Group)

