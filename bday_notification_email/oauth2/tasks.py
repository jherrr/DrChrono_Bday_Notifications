from __future__ import absolute_import

import json
import httplib2
from celery import shared_task

from oauth2client.contrib.django_orm import Storage

from .models import Doctor, CredentialsModel

@shared_task
def get_api_data():
    all_data = {}

    for doctor in Doctor.objects.all():
        storage = Storage(CredentialsModel, 'doctor_id', doctor.id, 'credential')
        credentials = storage.get()

        http = httplib2.Http()
        http = credentials.authorize(http)

        storage.put(credentials)
        (resp, content) = http.request("https://drchrono.com/api/patients",
        "GET")
        data = json.loads(content.decode("utf-8"))

        all_data[doctor.id] = data

    return all_data
