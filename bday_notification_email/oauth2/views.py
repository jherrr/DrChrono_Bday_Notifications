from django.shortcuts import render, redirect
from oauth2client.client import flow_from_clientsecrets

import os

import httplib2

# appending python path, get client_secrets.json to work
dir_name = os.path.dirname(__file__)
flow = flow_from_clientsecrets(
    os.path.join(dir_name, "client_secrets.json"),
    scope="patients:summary:read",
    redirect_uri="http://localhost:8000/oauth/auth_granted")

def auth_request(request):
    auth_uri = flow.step1_get_authorize_url()

    return redirect(auth_uri)

def oauth_entry(request):
    return render(request, "oauth_entry.html")

def auth_granted(request):
    get_params = request.GET

    try:
        if 'error' in get_params:
            raise ValueError('Error authorizing application: %s' % get_params[error])

        credentials = flow.step2_exchange(get_params["code"])

        http = httplib2.Http()
        http = credentials.authorize(http)

        (resp, content) = http.request("https://drchrono.com/api/patients_summary",
                    "GET")

        print(content)

    except ValueError as err:
        print('Handling run-time error: ', err)

    return render(request, "success.html")
