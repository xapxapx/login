# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-01 03:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0012_auto_20190501_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emchilgee',
            name='cos_review',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='emchilgee',
            name='doctor_review',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
    ]