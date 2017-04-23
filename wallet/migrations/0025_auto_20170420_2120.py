# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 21:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0024_auto_20170420_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='contacts',
        ),
        migrations.AddField(
            model_name='settings',
            name='contacts',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='wallet.Contacts'),
        ),
    ]
