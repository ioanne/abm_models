from django import forms
from apps.alumno.models import Alumno
from apps.profesor.models import Profesor


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = [
            'nombre',
            'apellido',
            'dni',
            'fecha_nacimiento',
            'email',
            'pepe'
        ]
