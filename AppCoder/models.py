from django.db import models

# Create your models here.

class Curso(models.Model):

    nombre = models.CharField('nombre',max_length=40)
    camada = models.IntegerField()

class Alumno(models.Model):

    nombre = models.CharField('nombre',max_length=50)
    apellido = models.CharField('apellido',max_length=50)
    fecha_inscripcion = models.DateField('fecha',auto_now=False,auto_now_add=False)
