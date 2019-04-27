#from django.db.models import Q  #duda si se borra o no
from django_filters.rest_framework import DjangoFilterBackend
import django_filters.rest_framework

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions
from .serializers import *
from .models import *
from django.contrib.auth.models import User

#uso de gmail
import smtplib
import email
import ssl

#prueba
#REST_FRAMEWORK = {
#    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
#}

class CrearPaciente(generics.ListCreateAPIView):

    def get_queryset(self):
        queryset = Paciente.objects.all()
        nombre = self.request.query_params.get('nombre', None)
        if nombre is not None:
             queryset = queryset.filter(nombre=nombre)
        print("\n\n\n",queryset)
        #gmail
        port = 587
        smtp_server = "smtp-mail.outlook.com"
        user = 'luis_bernardo_24@outlook.com'
        password = "bbkNOQ65"
        subject= "funciona?"
        message = """\
        Subject: oe

        Respondame por el celular si le llego."""
        conn = smtplib.SMTP(smtp_server,587)
        conn.ehlo()
        conn.starttls()
        conn.login(user,password)
        #for x in range(0,10):
        conn.sendmail(user,'jpgiraldor@eafit.edu.co',message)
        conn.quit
        return queryset


    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = []
    #filter_backends = (DjangoFilterBackend,)
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = ('id', 'nombre','apellidos','genero')
    #queryset = filter_queryset(queryset)
    #print("\n \n \n holaa  ",queryset)







    # def get_queryset(self, *args, **kargs):                #por si no me dejan usar filter, buscar como cambiar visualmente  filterset
    #     queryset_list= Paciente.objects.all()
    #     query= self.request.GET.get("q")
    #     if query:
    #         queryset_list = queryset_list.filter(
    #             Q(id__icontains=query)|
    #             Q(nombre__icontains=query)|
    #             Q(apellidos__icontains=query)|
    #             Q(fechanacimiento__icontains=query)|
    #             Q(genero__icontains=query)
    #             ).distinct()
    #     return queryset_list

class Getcitas(generics.ListCreateAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = CitaSerializer
    queryset = Cita.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('fechainicio', 'fechafin','fechareserva','paciente','doctor')

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
