from django.db import models

class Persona(models.Model):
  id = models.AutoField(primary_key = True)
  nombre = models.CharField(max_length = 100)
  apellido = models.CharField(max_length = 100)
  correo = models.EmailField(max_length = 100, unique = True)

  def __str__(self):
    return (self.nombre + " " + self.apellido)
