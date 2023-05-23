from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.profesor.forms import ProfesorForm


class ProfesorFormView(LoginRequiredMixin, CreateView):
    form_class = ProfesorForm
    template_name = 'profesor_create.html'
    success_url = reverse_lazy('alumno_inicio')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
