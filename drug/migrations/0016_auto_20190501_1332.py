# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-01 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0015_auto_20190501_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_review',
            name='emchilgee',
            field=models.IntegerField(default=0),
        ),
    ]
