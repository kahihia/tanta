# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-07 00:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0007_auto_20170407_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 7, 0, 25, 37, 904183, tzinfo=utc)),
        ),
    ]
