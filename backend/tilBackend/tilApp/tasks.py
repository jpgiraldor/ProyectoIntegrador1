from tilBackend.celery import app
import smtplib
import email
import ssl
#librerias pruebas
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from celery import Celery

@app.task
def correo():
    try:
        port = 587
        smtp_server = "smtp-mail.outlook.com"
        user = 'pythonzuluaga@outlook.com'
        password = "Python123"
        message ="""Subject: Asuntooooo\n
                    Y este es el mensaje
                    """
        conn = smtplib.SMTP(smtp_server,587)
        conn.ehlo()
        conn.starttls()
        conn.login(user,password)
        #for x in range(0,10):
        conn.sendmail(user,'lbzuluagag@eafit.edu.co',message)
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
