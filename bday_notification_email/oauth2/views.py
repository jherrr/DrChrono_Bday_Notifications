from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from oauth2client.client import flow_from_clientsecrets
from oauth2client.contrib.django_orm import Storage

import os
import httplib2
import json

from .models import Doctor, FlowModel, CredentialsModel

# appending python path, get client_secrets.json to work
dir_name = os.path.dirname(__file__)

def auth_request(request):
    session = request.session

    flow = flow_from_clientsecrets(
        os.path.join(dir_name, "client_secrets.json"),
        scope="patients:read",
        redirect_uri="http://localhost:8000/oauth/auth_granted")

    auth_uri = flow.step1_get_authorize_url()

    flow_obj = FlowModel(session_id = session.session_key, flow = flow)
    flow_obj.save()

    return redirect(auth_uri)

# session only saves after view is processed.
# must create session before auth_request
def oauth_entry(request):
    request.session["session_active"] = True
    return render(request, "oauth_entry.html")

def auth_granted(request):
    get_params = request.GET

    try:
        if 'error' in get_params:
            raise ValueError('Error authorizing application: %s' % get_params[error])

        session_key = request.session.session_key
        session = Session.objects.get(pk = session_key)
        flow_obj = FlowModel.objects.get(session_id = session)
        flow = flow_obj.flow

        credentials = flow.step2_exchange(get_params["code"])

        http = httplib2.Http()
        http = credentials.authorize(http)

        (resp, content) = http.request("https://drchrono.com/api/users/current",
        "GET")

        data = json.loads(content.decode("utf-8"))
        print(data)

        doctor_id = data['doctor']
        doctor = Doctor(pk = doctor_id)
        doctor.save()

        storage = Storage(CredentialsModel, 'doctor_id', doctor_id, "credential")
        storage.put(credentials)

    except ValueError as err:
        print('Handling run-time error: ', err)

    return render(request, "success.html")
