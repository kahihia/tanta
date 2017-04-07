# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 22:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_auto_20170404_2100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='create_date',
        ),
        migrations.AddField(
            model_name='post',
            name='create_dated',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 4, 22, 9, 3, 828116, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 4, 22, 9, 3, 829335, tzinfo=utc)),
        ),
    ]