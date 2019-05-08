# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-08 06:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0021_auto_20190506_0610'),
    ]

    operations = [
        migrations.CreateModel(
            name='Days_od_emchilgee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(default=django.utils.timezone.now)),
                ('is_done', models.BooleanField(default=False)),
                ('emchilgee', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='drug.Emchilgee')),
            ],
        ),
    ]