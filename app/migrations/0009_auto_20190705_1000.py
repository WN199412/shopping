# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-05 02:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20190705_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shangp',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 5, 10, 0, 33, 767195)),
        ),
        migrations.AlterField(
            model_name='user',
            name='regtime',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 5, 10, 0, 33, 763193)),
        ),
    ]