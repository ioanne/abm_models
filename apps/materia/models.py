from django.db import models

from abm_models.apps.utils.func_time import comienzo_materia, fin_materia


class MateriaAlumnoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
        )


class Materia(models.Model):
    nombre = models.CharField(max_length=50)
    profesor = models.ForeignKey(
        'profesor.Profesor',
        on_delete=models.CASCADE
    )
    alumnos = models.ManyToManyField(
        'alumno.Alumno',
        related_name="materias"
    )
    
    def __str__(self):
        return self.nombre


class MateriaAlumno(models.Model):
    materia = models.ForeignKey(
        'materia.Materia',
        on_delete=models.CASCADE
    )
    alumno = models.ForeignKey(
        'alumno.Alumno',
        on_delete=models.CASCADE
    )
    start_date = models.DateField(default=comienzo_materia, null=True)
    end_date = models.DateField(default=fin_materia, null=True)

    objects_all = models.Manager()
    objects = MateriaAlumnoManager()

    @classmethod
    def check_inscripcion(cls, alumno_id, materia_id):
        pass

    @classmethod
    def inscripcion(cls, alumno_id, materia_id):
        """Logica para la inscripcion de un alumno a una materia"""
        # 
        pass

    def __str__(self):
        return f'Materia: {self.materia.nombre} - Alumno: {self.alumno.nombre}'
