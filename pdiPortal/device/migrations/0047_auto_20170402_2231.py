# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-03 05:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0046_auto_20170331_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='facility',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='facility.Facility'),
        ),
    ]
