# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-18 02:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mlsx', '0019_auto_20190118_1014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_goods_list',
            name='pay_status',
        ),
        migrations.RemoveField(
            model_name='order_goods_list',
            name='send_status',
        ),
    ]