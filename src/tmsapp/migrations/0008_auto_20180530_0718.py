# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-05-30 07:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tmsapp', '0007_auto_20180530_0707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='task_name1',
            new_name='start_date',
        ),
    ]
