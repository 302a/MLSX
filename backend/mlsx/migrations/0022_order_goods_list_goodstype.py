# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-18 02:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlsx', '0021_remove_order_goods_list_pay_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_goods_list',
            name='goodstype',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]