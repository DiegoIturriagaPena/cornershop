# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 16:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20170720_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 20, 16, 3, 25, 82849)),
        ),
        migrations.AlterField(
            model_name='menu',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 20, 16, 3, 25, 82901)),
        ),
    ]