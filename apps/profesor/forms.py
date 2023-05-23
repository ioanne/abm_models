from django import forms

from apps.profesor.models import Profesor


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = [
            'nombre',
            'apellido',
            'dni',
            'fecha_nacimiento',
            'email',
            'pepe'
        ]
