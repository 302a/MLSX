# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-17 01:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlsx', '0003_market'),
    ]

    operations = [
        migrations.AddField(
            model_name='market',
            name='goods_price',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='market',
            name='goods_vip_price',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='enquiry',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_num',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='vip_end_time',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='vip_start_time',
            field=models.TextField(null=True),
        ),
    ]
