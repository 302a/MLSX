# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-18 02:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlsx', '0018_auto_20190118_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_goods_list',
            name='create_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='order_goods_list',
            name='pay_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='order_goods_list',
            name='update_time',
            field=models.DateTimeField(),
        ),
    ]
