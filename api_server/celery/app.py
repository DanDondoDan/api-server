import os
from celery import Celery
from api_server.celery.schedule import CELERY_BEAT_SCHEDULE


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_server.settings')
app = Celery("api_server")
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.beat_schedule = CELERY_BEAT_SCHEDULE

app.autodiscover_tasks()