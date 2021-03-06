# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 13:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20170329_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='total_distance',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='bid',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Job'),
        ),
    ]
