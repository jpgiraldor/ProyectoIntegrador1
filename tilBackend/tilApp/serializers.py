from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *

User=get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type':'password'},write_only=True)
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = User
        fields= [
            "username",
            "email",
            "password",
            "password2"
        ]
    def validate(self,data):
        pw=data.get("password")
        pw2=data.get("password2")
        if pw != pw2:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        return data


class PacienteSerializer(serializers.ModelSerializer):
    usuario=UserSerializer(many=False)

    class Meta:
        model =Paciente
        fields=[
            'cedula',
            "usuario",
            "nombre",
            "apellidos",
            "fechanacimiento",
            "genero"
        ]

    def create(self, validated_data):
        print("validando...")
        print(validated_data)
        user=validated_data.pop('usuario')
        user_object=User(username=user.get('username'), email=user.get('email'))
        user_object.set_password(user.get('password'))
        user_object.save()
        paciente = Paciente(usuario=user_object,
                            cedula=validated_data.get('cedula'),
                            nombre=validated_data.get('nombre'),
                            apellidos=validated_data.get('apellidos'),
                            fechanacimiento = validated_data.get('fechanacimiento'),
                            genero = validated_data.get('genero'))
        paciente.save()
        return paciente

class EspecializacionSerializer(serializers.ModelSerializer):


    class Meta:
        model=Especializacion
        fields=[
        "nombre"
        ]

    def create(self, validated_data):
        print("validando...")
        print(validated_data)
        especializacion=Especializacion(nombre=validated_data.get('nombre'))
        especializacion.save()
        return especializacion

class DoctorSerializer(serializers.ModelSerializer):
    usuario=UserSerializer(many=False)
    #especializacion=serializers.StringRelatedField(many=False)

    class Meta:
        model =Doctor
        fields=[
            "usuario",
            "nombre",
            "apellidos",
            "especializacion",
        ]

    def create(self, validated_data):
        print("Validando...")
        print(validated_data)
        espec=validated_data.pop('especializacion')
        user=validated_data.pop('usuario')
        user_object=User(username=user.get('username'), email=user.get('email'))
        user_object.set_password(user.get('password'))
        user_object.save()
        doctor= Doctor(usuario= user_object,
        nombre= validated_data.get('nombre'),
        apellidos= validated_data.get('apellidos'),
        especializacion=espec)
        doctor.save()
        return doctor

class CitaSerializer(serializers.ModelSerializer):

    class Meta:
        model=Cita
        fields=[
            'id',
            'fechainicio',
            'fechafin',
            'fechareserva',
            'paciente',
            'doctor'
        ]

    def create(self, validated_data):
        print("validando..........................................................................")
        print(validated_data)
        print("------------------------------------------------------------------------")
        doc=validated_data.pop('doctor')
        pac=validated_data.pop('paciente')
        cita = Cita(
        fechainicio=validated_data.get('fechainicio'),
        fechafin=validated_data.get('fechafin'),
        fechareserva = validated_data.get('fechareserva'),
        paciente=pac,
        doctor=doc)
        cita.save()
        return cita
