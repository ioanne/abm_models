from django.contrib import admin

from apps.profesor.models import Profesor


@admin.register(Profesor)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dni')
    search_fields = ('dni',)
    list_filter = ('dni',)
