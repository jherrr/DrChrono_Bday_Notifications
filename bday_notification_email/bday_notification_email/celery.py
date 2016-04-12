from __future__ import absolute_import
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bday_notification_email.settings')

from django.conf import settings  # noqa

app = Celery('bday_notification_email')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
# app.autodiscover_tasks(['bday_notification_email', 'send_email', 'oauth2'], force=True)
app.autodiscover_tasks(['bday_notification_email', 'send_email', 'oauth2'])

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
