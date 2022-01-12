#Lo cree yo.

from django.urls import path
from AppCoder.models import Curso
from AppCoder import views

urlpatterns = [
    path('crea-curso',views.crea_curso),
    path('', views.inicio),
    path('curso', views.curso),
    path('profesores', views.profesores),
    path('estudiantes', views.estudiantes),
    path('entregables', views.entregables)
  
]