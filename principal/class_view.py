from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from .models import Persona
from .forms import PersonForm

class ListPerson(ListView):
  model = Persona
  template_name = 'ppal.html'

  def get_queryset(self):
    return self.model.objects.all()

class CreatePerson(CreateView):
  model = Persona
  form_class = PersonForm
  template_name = 'create_person.html'
  success_url = reverse_lazy('ppal')

class UpdatePerson(UpdateView):
  model = Persona
  form_class = PersonForm
  template_name = 'create_person.html'
  success_url = reverse_lazy('ppal')

class DeletePerson(DeleteView):
  model = Persona
  template_name = 'verify.html'
  success_url = reverse_lazy('ppal')