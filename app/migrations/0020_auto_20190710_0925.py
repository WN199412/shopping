# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-10 01:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20190709_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manage',
            name='time',
            field=models.CharField(default=datetime.datetime(2019, 7, 10, 9, 25, 11, 431804), max_length=30),
        ),
        migrations.AlterField(
            model_name='shangp',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 10, 9, 25, 11, 434808)),
        ),
        migrations.AlterField(
            model_name='user',
            name='regtime',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 10, 9, 25, 11, 430803)),
        ),
    ]
