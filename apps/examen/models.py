from django.db import models, transaction

from datetime import datetime


class Examen(models.Model):
    fecha = models.DateField(default=datetime.now)
    materia = models.ForeignKey(
        'materia.Materia',
        on_delete=models.CASCADE
    ) # Almacena la Clave Foraña
    profesor = models.ForeignKey(
        'profesor.Profesor',
        on_delete=models.CASCADE
    ) # Almacena la clave foraña
    titulo = models.CharField(default="", max_length=50)
    descripcion = models.TextField(default="")

    def realizar_examen(self):
        with transaction.atomic():
            pass

    def __str__(self):
        return f'Nombre: {self.materia.nombre} Fecha: {self.fecha}'


class ContenidoExamen(models.Model):
    examen = models.ForeignKey(
        'examen.Examen',
        on_delete=models.CASCADE
    )
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    respuesta = models.TextField()
    puntaje = models.IntegerField()

    def __str__(self):
        return f'Contenido: {self.id} - {self.puntaje}'


# class ExamenAlumno(models.Model):
#     alumno = models.ForeignKey(
#         'alumno.Alumno',
#         on_delete=models.CASCADE
#     )
#     examen = models.ForeignKey(
#         'examen.Examen',
#         on_delete=models.CASCADE
#     )
#     nota = models.IntegerField()

#     def __str__(self):
#         return f'Alumno: {self.alumno.id} Examen: {self.examen.id} Nota: {self.nota}'
