from __future__ import absolute_import

import json
import httplib2
from celery import shared_task

from oauth2client.contrib.django_orm import Storage

from .models import Doctor, CredentialsModel

@shared_task
def get_api_data():
    for doctor in Doctor.objects.all():
        storage = Storage(CredentialsModel, 'doctor_id', doctor.id, 'credential')
        print("doctor.id: ", doctor.id)
        credentials = storage.get()

        http = httplib2.Http()
        http = credentials.authorize(http)

        (resp, content) = http.request("https://drchrono.com/api/patients",
        "GET")

        print(content)

        data = json.loads(content.decode("utf-8"))
