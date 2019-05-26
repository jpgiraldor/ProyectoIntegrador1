from tilBackend.celery import app
from datetime import timedelta
import datetime
import smtplib
import email
import ssl
from .models import *
#librerias pruebas
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from celery import Celery
from os import system, name


@app.task
def correo():
    hora = datetime.datetime.now()
    queryset = Cita.objects.all()
    queryset = queryset.filter(fechainicio__gte=hora)
    hora +=timedelta(days=1)
    queryset = queryset.filter(fechainicio__lte=hora)
    for x in queryset:
        usuario=x.paciente
        usuario=usuario.usuario.email
        #system('clear')
        try:
            port = 587
            smtp_server = "smtp-mail.outlook.com"
            user = 'luis_bernardo_24@outlook.com'
            password = "bbkNOQ65"
            message ="""Subject:Correo enviado desde python\n
                        funciona123
                        """

            conn = smtplib.SMTP(smtp_server,587)
            conn.ehlo()
            conn.starttls()
            conn.login(user,password)
            conn.sendmail(user,usuario,message)
            conn.quit
        except:
            print("Algo fallo")




def task_correo():
    """
    envia correo
    """
    correo()
    logger.info("se envio el correo")



app.conf.update
