from django.contrib.sessions.models import Session
from django.db import models
from oauth2client.contrib.django_orm import FlowField
from oauth2client.contrib.django_orm import CredentialsField

from importlib import import_module
from django.conf import settings

class FlowModel(models.Model):
    session = models.ForeignKey(Session, primary_key=True)
    flow = FlowField()

class CredentialsModel(models.Model):
    session = models.ForeignKey(Session, primary_key=True)
    credential = CredentialsField()
