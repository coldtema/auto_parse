import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'encar_parse.settings')

app = Celery('encar_parse')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()