# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-17 01:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlsx', '0004_auto_20190117_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='enquiry',
            field=models.TextField(default=0),
        ),
    ]