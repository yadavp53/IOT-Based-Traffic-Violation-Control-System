from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tracker.settings')

app1 = Celery('Tracker')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app1.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app1.autodiscover_tasks()