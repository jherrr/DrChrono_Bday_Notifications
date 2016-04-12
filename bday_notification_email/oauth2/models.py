from django.contrib.sessions.models import Session
from django.db import models
from oauth2client.contrib.django_orm import FlowField
from oauth2client.contrib.django_orm import CredentialsField

class Doctor(models.Model):
    id = models.CharField(max_length = 8, primary_key = True)

class FlowModel(models.Model):
    session = models.ForeignKey(Session, primary_key = True)
    flow = FlowField()

class CredentialsModel(models.Model):
    doctor = models.ForeignKey(Doctor, primary_key = True)
    credential = CredentialsField()
