# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-02 12:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=100)),
                ('order', models.IntegerField(default=1)),
                ('state', models.IntegerField(default=1)),
                ('time', models.DateTimeField(max_length=100)),
            ],
            options={
                'db_table': 'ad',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('aname', models.CharField(max_length=15)),
                ('iphone', models.CharField(max_length=15)),
                ('pro', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('area', models.CharField(max_length=30)),
                ('disarea', models.CharField(max_length=30)),
                ('detaddress', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField(default=0)),
                ('time', models.DateTimeField(max_length=30)),
                ('isdef', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('oid', models.AutoField(primary_key=True, serialize=False)),
                ('oname', models.CharField(max_length=30)),
                ('cate', models.IntegerField(default=0)),
                ('path', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'goods',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('gid', models.IntegerField()),
                ('time', models.DateTimeField(max_length=100)),
            ],
            options={
                'db_table': 'collection',
            },
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'details',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('logid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('logip', models.CharField(max_length=30)),
                ('time', models.DateTimeField(max_length=30)),
            ],
            options={
                'db_table': 'log',
            },
        ),
        migrations.CreateModel(
            name='Manage',
            fields=[
                ('mid', models.AutoField(primary_key=True, serialize=False)),
                ('managername', models.CharField(max_length=30)),
                ('managerpassword', models.CharField(max_length=30)),
                ('sex', models.CharField(default=0, max_length=10, null=True)),
                ('type', models.IntegerField(default=0)),
                ('old', models.CharField(default=0, max_length=10)),
                ('iphone', models.CharField(default=0, max_length=30, null=True)),
                ('email', models.CharField(max_length=30, null=True)),
                ('qq', models.CharField(max_length=20, null=True)),
                ('time', models.CharField(max_length=30, null=True)),
                ('xinxi', models.CharField(max_length=500, null=True)),
            ],
            options={
                'db_table': 'manage',
            },
        ),
        migrations.CreateModel(
            name='Mdelu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mid', models.IntegerField(default=0, null=True)),
                ('name', models.CharField(max_length=20, null=True)),
                ('ip', models.CharField(max_length=20, null=True)),
                ('time', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'mdelu',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('oid', models.AutoField(primary_key=True, serialize=False)),
                ('sid', models.IntegerField(null=True)),
                ('orderid', models.IntegerField(null=True)),
                ('much', models.IntegerField(null=True)),
                ('orderDate', models.CharField(max_length=30, null=True)),
                ('orderState', models.IntegerField(default=1, null=True)),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Shangp',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('Ocategory', models.IntegerField(default=0)),
                ('Tcategory', models.IntegerField(default=0)),
                ('Scategory', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=100)),
                ('keyword', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=300)),
                ('price', models.IntegerField(default=0)),
                ('isshow', models.IntegerField(default=1)),
                ('number', models.IntegerField(default=0)),
                ('soldnum', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'shangp',
            },
        ),
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cid', models.IntegerField(default=0)),
                ('sid', models.IntegerField(default=0)),
                ('time', models.DateTimeField(max_length=30)),
                ('number', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'shopping',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('md', models.IntegerField(default=0)),
                ('path', models.CharField(max_length=100)),
                ('gid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Shangp')),
            ],
            options={
                'db_table': 'size',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=60)),
                ('Realname', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=32)),
                ('type', models.IntegerField(default=0)),
                ('email', models.CharField(max_length=30)),
                ('sex', models.IntegerField(default=0)),
                ('birthday', models.CharField(max_length=30, null=True)),
                ('phone', models.CharField(max_length=30, null=True)),
                ('city', models.CharField(max_length=60, null=True)),
                ('regtime', models.DateTimeField(default=datetime.datetime(2019, 7, 2, 20, 28, 35, 776166))),
                ('level', models.CharField(default='青铜', max_length=60)),
                ('regip', models.CharField(max_length=30)),
                ('logip', models.CharField(max_length=30)),
                ('gold', models.IntegerField(default=10)),
                ('islog', models.IntegerField(default=1)),
                ('lcon', models.CharField(default=0, max_length=200)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.AddField(
            model_name='shopping',
            name='uid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
        migrations.AddField(
            model_name='order',
            name='uid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
        migrations.AddField(
            model_name='details',
            name='gid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Shangp'),
        ),
        migrations.AddField(
            model_name='collection',
            name='uid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
        migrations.AddField(
            model_name='address',
            name='uid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
    ]
