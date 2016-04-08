from django.shortcuts import render, redirect
from oauth2client.client import flow_from_clientsecrets

import os

import datetime, pytz, requests

# appending python path, get client_secrets.json to work
dir_name = os.path.dirname(__file__)

def auth_request(request):
    flow = flow_from_clientsecrets(
        os.path.join(dir_name, "client_secrets.json"),
        scope="patients:summary:read",
        redirect_uri="http://localhost:8000/oauth/auth_granted")
    auth_uri = flow.step1_get_authorize_url()

    return redirect(auth_uri)

def oauth_entry(request):
    return render(request, "oauth_entry.html")

def auth_granted(request):
    get_params = request.GET

    try:
        if 'error' in get_params:
            raise ValueError('Error authorizing application: %s' % get_params[error])

        response = requests.post('https://drchrono.com/o/token/', data={
            'code': get_params['code'],
            'grant_type': 'authorization_code',
            'redirect_uri': 'REDIRECT_URI',
            'client_id': 'CLIENT_ID',
            'client_secret': 'CLIENT_SECRET',
        })
        response.raise_for_status()
        data = response.json()

        # Save these in your database associated with the user
        access_token = data['access_token']
        refresh_token = data['refresh_token']
        expires_timestamp = datetime.datetime.now(pytz.utc) + datetime.timedelta(seconds=data['expires_in'])
    except ValueError as err:
        print('Handling run-time error: ', err)

    return render(request, "success.html")
