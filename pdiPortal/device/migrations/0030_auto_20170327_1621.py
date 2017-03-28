# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 23:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0029_auto_20170224_1825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devicemodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='device',
            name='facility',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='facility.Facility'),
        ),
        migrations.AlterField(
            model_name='devicemodel',
            name='device_model',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
    ]
