# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 22:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0017_auto_20170415_2222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactions',
            old_name='user',
            new_name='fx',
        ),
    ]
