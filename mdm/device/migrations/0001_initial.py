# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 17:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Android Device', max_length=100)),
                ('androidId', models.CharField(max_length=25)),
                ('buildNumber', models.CharField(max_length=25)),
                ('osVersion', models.CharField(max_length=25)),
                ('heartbeat', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_model', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='downloadedApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('downloadedDate', models.DateTimeField(auto_now_add=True)),
                ('renewalDate', models.DateField(default=django.utils.timezone.now)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.Device')),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='device_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.DeviceModel'),
        ),
    ]