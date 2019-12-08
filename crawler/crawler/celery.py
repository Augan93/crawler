# from __future__ import absolute_import, unicode_literals
import os
import django
from celery import Celery


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crawler.settings')
django.setup()
app = Celery('crawler')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.

app.config_from_object('django.conf:settings')
# app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'news.tasks.hello',
        'schedule': 5,  # execute every 30 second
        # 'args': (16, 16)
    },
}
app.conf.timezone = 'UTC'
