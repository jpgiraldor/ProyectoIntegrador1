#from django.db.models import Q  #duda si se borra o no
from django_filters.rest_framework import DjangoFilterBackend
import django_filters.rest_framework
from django.views.generic import DeleteView
from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions
from .serializers import *
from .models import *
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
#angular
import json
#from django.views.generics import View, TemplateView, FormView


#uso de gmail
import smtplib
import email
import ssl



class CrearPaciente(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = []
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = ('cedula', 'nombre','apellidos','genero')


class Getcitas(generics.ListCreateAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = CitaSerializer
    queryset = Cita.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id','fechainicio', 'fechafin','fechareserva','paciente','doctor')

class Deletecitas(generics.RetrieveDestroyAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = CitaSerializer
    queryset = Cita.objects.all()



class CrearEspecializacion(generics.ListCreateAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = EspecializacionSerializer
    queryset = Especializacion.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('')

class CrearDoctor(generics.ListCreateAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('nombre','apellidos','especializacion')

# Create your views here.
#soapui
#restadvanced
