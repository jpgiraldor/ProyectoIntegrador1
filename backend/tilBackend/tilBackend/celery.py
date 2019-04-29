from __future__ import absolute_import, unicode_literals
import os
import sys
from celery import Celery
from celery._state import _set_current_app
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tilBackend.settings')
app = Celery('tilBackend')
app.config_from_object('django.conf:settings', namespace='CELERY')
_set_current_app(app) 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../tilBackend')))
django.setup()
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(
    BROKER_URL = 'redis://localhost:6379/0',
)
