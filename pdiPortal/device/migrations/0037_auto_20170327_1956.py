# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 02:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0036_auto_20170327_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='id',
        ),
        migrations.AlterField(
            model_name='device',
            name='android_id',
            field=models.CharField(max_length=25, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='devicefacilitylist',
            name='facility',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.Facility'),
        ),
    ]
