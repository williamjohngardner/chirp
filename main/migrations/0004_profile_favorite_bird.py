# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorite_bird',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
