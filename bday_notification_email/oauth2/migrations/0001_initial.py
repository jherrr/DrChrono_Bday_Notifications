# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-11 02:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import oauth2client.contrib.django_orm


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sessions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CredentialsModel',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='sessions.Session')),
                ('credential', oauth2client.contrib.django_orm.CredentialsField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FlowModel',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='sessions.Session')),
                ('flow', oauth2client.contrib.django_orm.FlowField(null=True)),
            ],
        ),
    ]
