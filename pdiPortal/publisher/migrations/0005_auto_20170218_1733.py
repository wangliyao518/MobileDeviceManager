# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 01:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0004_auto_20170218_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='title',
            new_name='application_title',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='title',
            new_name='review_title',
        ),
    ]