from django.shortcuts import render
from django.http import HttpResponse
import django
from django.conf import settings

import datetime

from send_email import tasks

def index(request):
    return render(request, 'index.html')


def success(request):
    email = request.POST.get('email', '')
    data = """
Hello there!

I wanted to personally write an email in order to welcome you to our platform.\
 We have worked day and night to ensure that you get the best service. I hope \
that you will continue to use our service. We send out a newsletter once a \
week. Make sure that you read it. It is usually very informative.

Cheers!
~ Yasoob
    """

    result = tasks.send_email.apply_async(args=[email, data]
        , eta=datetime.datetime(2016, 3, 30, 7, 15))
    return render(request, 'success.html')
