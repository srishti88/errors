# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sign_up',
            fields=[
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=120)),
                ('username', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=40)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
