# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 01:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_auto_20170218_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portaluser',
            name='facility',
            field=models.ManyToManyField(to='facility.Facility'),
        ),
    ]
