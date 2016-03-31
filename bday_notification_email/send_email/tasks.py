from __future__ import absolute_import

from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_email(email, data):

    return send_mail('Welcome!', data, "Yasoob",
              [email], fail_silently=False)
