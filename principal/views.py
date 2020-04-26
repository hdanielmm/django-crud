from django.shortcuts import render, redirect
from .models import Persona
from .forms import PersonForm

def inicio(request):
  personas_from_db = Persona.objects.all() # select * from Persona
  
  context = {
    'personas_from_context': personas_from_db
  }
  
  return render(request, 'ppal.html', context)

def createPerson(request):
  
  if request.method == 'GET':
    form = PersonForm()

    context = {
      'form_from_context': form
    }
  else: 
    form = PersonForm(request.POST)

    context = {
      'form_from_context': form
    }

    if form.is_valid():
      form.save()
      return redirect('ppal')

  return render(request, 'create_person.html', context)

def editPerson(request, id):
  persona = Persona.objects.get(id = id)

  if request.method == 'GET':
    form = PersonForm(instance = persona)
    
    context = {
      'form_from_context': form
    }
  else:
    form = PersonForm(request.POST, instance = persona)

    context = {
      'form_from_context': form
    }

    if form.is_valid():
      form.save()
      return redirect('ppal')

  return render(request, 'create_person.html', context)

def deletePerson(request, id):
  persona = Persona.objects.get(id = id)
  persona.delete()
  return redirect('ppal')