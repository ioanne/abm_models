from django.contrib import admin

from apps.custom_user.models import CustomUser


@admin.register(CustomUser)
class AlumnoAdmin(admin.ModelAdmin):
    pass
