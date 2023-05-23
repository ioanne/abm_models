from django.db import models

from apps.custom_user.models import CustomUser


class PersonaManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().exclude(
            deleted_at__isnull=False,
            active=False
        )


class Persona(models.Model):
    class Meta:
        # Significa que no se va a crear una tabla llamada Persona.
        abstract = True
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)
    active = models.BooleanField(default=True)
    pepe = models.IntegerField(default=20)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)

    objects_all = models.Manager()
    objects = PersonaManager()

    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.dni}'
