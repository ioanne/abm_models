from django.contrib import admin

from apps.alumno.models import Alumno


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dni')
    search_fields = ('dni',)
    list_filter = ('dni',)
