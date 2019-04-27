from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^registroPaciente', CrearPaciente.as_view()),
    url(r'^cita', Getcitas.as_view()),
    url(r'^registroEspecializacion', CrearEspecializacion.as_view() ),
    url(r'^registroDoctor',CrearDoctor.as_view()),

]
