# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 16:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import publisher.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('device', '0003_auto_20170130_0858'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('version', models.CharField(max_length=40)),
                ('partNumber', models.CharField(max_length=15)),
                ('pricePerMonth', models.FloatField()),
                ('msrp', models.FloatField()),
                ('description', models.TextField()),
                ('recent_updates', models.TextField(null=True)),
                ('icon', models.ImageField(upload_to=publisher.models.app_directory_path)),
                ('banner', models.ImageField(upload_to=publisher.models.app_directory_path)),
                ('applicationFile', models.FileField(upload_to=publisher.models.app_directory_path)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('number_of_downloads', models.PositiveIntegerField(default=0)),
                ('developer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AppModelList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publisher.Application')),
                ('device_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.DeviceModel')),
            ],
        ),
        migrations.CreateModel(
            name='AppPlatformList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publisher.Application')),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('icon', models.ImageField(upload_to=publisher.models.platform_path)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('body', models.TextField(max_length=1000)),
                ('rating', models.PositiveIntegerField(null=True)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publisher.Application')),
            ],
        ),
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=publisher.models.app_directory_path)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publisher.Application')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to=publisher.models.app_directory_path)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publisher.Application')),
            ],
        ),
        migrations.AddField(
            model_name='appplatformlist',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publisher.Platform'),
        ),
        migrations.AddField(
            model_name='application',
            name='platform',
            field=models.ManyToManyField(through='publisher.AppPlatformList', to='publisher.Platform'),
        ),
        migrations.AddField(
            model_name='application',
            name='valid_device_models',
            field=models.ManyToManyField(through='publisher.AppModelList', to='device.DeviceModel'),
        ),
    ]
