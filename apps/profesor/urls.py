from django.urls import path

from apps.profesor.views import ProfesorFormView


urlpatterns = [
    path("crear-profesor", ProfesorFormView.as_view(), name="crear_profesor")
]