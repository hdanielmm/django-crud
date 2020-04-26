from django import  forms
from .models import Persona

class PersonForm(forms.ModelForm):
  class Meta:
    model = Persona
    fields = '__all__'
    #fields = ('nombre', 'apellido', 'correo',)