from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.oauth_entry, name = 'oauth_entry'),
    url(r'^auth_request', views.auth_request, name = 'auth_request'),
    url(r'^auth_granted', views.auth_granted, name = 'auth_granted'),
]
