from datetime import datetime

from django.db import models

from apps.utils.models import Persona


class Profesor(Persona):
    fecha_alta = models.DateField(default=datetime.now)

    def __str__(self):
        algo = super().__str__()
        return f'Profesor: {algo}'