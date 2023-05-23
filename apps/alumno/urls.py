from django.urls import path

from apps.alumno.views import AlumnoView, AlumnosView, AlumnoFormView


urlpatterns = [
    path("", AlumnosView.as_view(), name="alumno_inicio"),
    path("<int:id>", AlumnoView.as_view(), name="alumno"),
    path("crear", AlumnoFormView.as_view(), name="crear_alumno"),
]