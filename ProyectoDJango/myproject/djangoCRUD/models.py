from django.db import models

# Create your models here.
class Registros(models.Model):
  id = models.AutoField(primary_key=True)
  nombres = models.CharField(max_length=30)
  apellidos = models.CharField(max_length=30)
  correo = models.CharField(max_length=30)
  materia = models.CharField(max_length=30)

  def __str__(self):
    texto = "{0} {1}"
    return texto.format(self.nombres, self.apellidos)
