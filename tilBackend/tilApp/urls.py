from django.conf.urls import url
from .views import *
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^registroPaciente', CrearPaciente.as_view()),
    url(r'^cita', Getcitas.as_view()),
    url(r'^Deletecita/(?P<pk>\d+)/$', Deletecitas.as_view()),
    url(r'^registroEspecializacion', CrearEspecializacion.as_view() ),
    url(r'^registroDoctor',CrearDoctor.as_view()),
]
