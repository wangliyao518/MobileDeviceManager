# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 01:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0016_auto_20170218_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='facility',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='facility.Facility'),
        ),
    ]
