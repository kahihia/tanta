# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0033_remove_contacts_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='groups',
            field=models.ManyToManyField(to='wallet.Group'),
        ),
    ]
