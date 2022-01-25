from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse
from AppCoder.forms import CursoFormulario
from AppCoder.models import Profesor




# Create your views here.

def crea_curso(self):
    
    curso=Curso(nombre="JavaScript",camada=23456)
    
    curso.save()

    return HttpResponse(f'Se creo el curso de {curso.nombre} con el nro de camada {curso.camada}')

def cursoFormulario(req):

    if (req.method == 'POST'):

        mi_formulario = CursoFormulario(req.POST)
        if (mi_formulario.is_valid()):

            informacion = mi_formulario.cleaned_data
            curso = Curso(nombre=informacion["nombre"], camada=informacion["camada"])
            curso.save()

            return render(req,'AppCoder/inicio.html')
    else:
         mi_formulario=CursoFormulario()
        

    return render(req, 'AppCoder/cursoFormulario.html', {'form':mi_formulario})

def busquedaCamada(req):
    return render(req, "AppCoder/busquedaCamada.html")

def buscar(request):

    if (request.method == 'GET'):
        camada = request.GET["camada"]
        cursos= Curso.objects.filter(camada=camada)

        return render(request, "AppCoder/cursos.html",{'cursos':cursos, 'camada':camada})
    else:

        return HttpResponse('No enviaste datos')


def inicio(req):

    return render(req, 'AppCoder/inicio.html')

def curso(req):

    return render(req,'AppCoder/cursos.html')

def lista_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, "AppCoder/lista_profesores.html",{'profesores':profesores})

def profesores(request):

    if (request.method == 'POST'):
        
        mi_formulario = ProfesorFormulario(request.POST)

        if mi_formulario.is_valid():

            data= mi_formulario.cleaned_data
            profesor = Profesor(nombre=data["nombre"],apellido=data["apellido"],email=data["email"], profesion=data["profesion"])
            profesor.save()

            return render(request, "AppCoder/inicio.html")
        
        else:
            mi_formulario=ProfesorFormulario()
            return render(request, "AppCoder/profesores.html",{"form":mi_formulario})


def estudiantes(req):

    return render(req,'AppCoder/estudiantes.html')

def entregables(req):

    return render(req,'AppCoder/entregables.html')

