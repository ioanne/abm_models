from django.db import models


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

    objects_all = models.Manager()
    objects = PersonaManager()

    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.dni}'
