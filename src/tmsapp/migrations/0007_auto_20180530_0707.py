# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-05-30 07:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tmsapp', '0006_auto_20180530_0654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='activity_number',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='task_name',
        ),
        migrations.AddField(
            model_name='assignment',
            name='task_name1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tmsapp.Task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_name',
            field=models.CharField(max_length=120, verbose_name='accounts.MyUser'),
        ),
    ]