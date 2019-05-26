from django.db import models
from django.contrib.auth.models import User

class Especializacion(models.Model):
    nombre=models.CharField(max_length=30,unique=True)

    def __str__(self):
        return "{0}".format(self.nombre)

class Doctor(models.Model):
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    nombre=models.CharField(primary_key=True, unique=True, max_length=60)
    apellidos=models.CharField(max_length=60)
    especializacion=models.ForeignKey(Especializacion,on_delete=models.CASCADE)

    def __str__(self):
        return "{0} {1}".format(self.apellidos, self.nombre)

class Paciente(models.Model):
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    cedula=models.IntegerField(primary_key=True, unique=True)
    nombre=models.CharField(max_length=60)
    apellidos=models.CharField(max_length=60)
    fechanacimiento=models.DateField()
    GENERO=(('M','Masculino'),('F','Femenino'))
    genero=models.CharField(choices=GENERO,max_length=100)

    def __str__(self):
        return "{0} {1}".format(self.apellidos, self.nombre)

class Cita(models.Model):
    fechainicio=models.DateTimeField()
    fechafin=models.DateTimeField()
    fechareserva=models.DateTimeField()
    paciente=(models.ForeignKey(Paciente,on_delete=models.CASCADE))
    doctor=(models.ForeignKey(Doctor,on_delete=models.CASCADE))

    def __str__(self):
        return "Paciente {0} fecha {1}".format(self.paciente, self.fechainicio)



# Create your models here.
