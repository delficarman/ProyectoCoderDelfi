from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

# Create your views here.

def crea_curso(self):
    
    curso=Curso(nombre="JavaScript",camada=23456)
    
    curso.save()

    return HttpResponse(f'Se creo el curso de {curso.nombre} con el nro de camada {curso.camada}')

def inicio(req):

    return render(req, 'AppCoder/inicio.html')

def curso(req):

    return render(req,'AppCoder/cursos.html')

def profesores(req):

    return render(req,'AppCoder/profesores.html')

def estudiantes(req):

    return render(req,'AppCoder/estudiantes.html')

def entregables(req):

    return render(req,'AppCoder/entregables.html')
