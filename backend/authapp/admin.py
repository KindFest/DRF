from django.contrib import admin
from authapp import models
from django.contrib.auth.admin import UserAdmin


@admin.register(models.Users)
class CustomUserModelAdmin(UserAdmin):
    pass
# admin.site.register(models.Users)
