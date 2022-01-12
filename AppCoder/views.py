from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

# Create your views here.

def crea_curso(self):
    
    curso=Curso(nombre="JavaScript",camada=23456)
    
    curso.save()

    return HttpResponse(f'Se creo el curso de {curso.nombre} con el nro de camada {curso.camada}')

