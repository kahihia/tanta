# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-07 18:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_auto_20170407_0025'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TantaWallet',
            new_name='Wallet',
        ),
    ]