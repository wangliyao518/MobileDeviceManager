# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 02:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0002_auto_20170125_1046'),
        ('device', '0033_auto_20170327_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceFacilityList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.Device')),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.Facility')),
            ],
        ),
    ]
