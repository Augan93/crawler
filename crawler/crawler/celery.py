import os
import django
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crawler.settings')
django.setup()
app = Celery('crawler')


app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'get-news-every-30-minutes': {
        'task': 'news.tasks.get_news',
        'schedule': 5,  # execute every 1800 second
    },
}
app.conf.timezone = 'UTC'
