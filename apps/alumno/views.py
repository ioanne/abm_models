# Imports sin from del sistema o de django.
import os

# Imports de python 
from datetime import datetime

# Imports de django o librerias de terceros
from django.shortcuts import render
from django.views.generic.base import (
    TemplateView,
    View
)

# Nuestro import sin from
import algo

# Imports de nuestras apps
from apps.alumno.models import Alumnos

# Todos los importas van ordenados alfabeticamente


# backendifts/alumno
class AlumnoView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # Autorizacion
        user = self.request.user
        materias = user.alumno.materias.all()

# backendifts/alumno/<int: id>
class AlumnoView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # Autorizacion
        alumno = Alumnos.objects.get(id=kwargs['id'])
        materias = alumno.materias.all()
