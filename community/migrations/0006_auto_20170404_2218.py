# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 22:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0005_auto_20170404_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 4, 22, 18, 36, 614149, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_dated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]