#Lo cree yo.

from django.urls import path
from AppCoder.models import Curso
from AppCoder import views

urlpatterns = [
    path('crea-curso',views.crea_curso),
    path('inicio', views.inicio,name="inicio"),
    path('curso', views.curso,name="curso"),
    path('profesores', views.profesores,name="profesores"),
    path('estudiantes', views.estudiantes,name="estudiantes"),
    path('entregables', views.entregables,name="entregables"),
    path('cursoFormulario/',views.cursoFormulario,name="cursoFormulario"),
    path('busquedaCamada/',views.busquedaCamada,name="BusquedaCamada"),
    path('buscar/',views.buscar,name="buscar"),
    path('lista_profesores/',views.lista_profesores ,name="lista_profesores")
  
]