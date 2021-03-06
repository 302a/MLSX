# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-17 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlsx', '0012_auto_20190117_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='dry_fruit_goods',
            name='sales',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='dry_fruit_goods',
            name='storage',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='food_goods',
            name='sales',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='food_goods',
            name='storage',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='fresh_goods',
            name='sales',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='fresh_goods',
            name='storage',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='fruit_goods',
            name='sales',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='fruit_goods',
            name='storage',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='meat_goods',
            name='sales',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='meat_goods',
            name='storage',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='nofood_goods',
            name='sales',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='nofood_goods',
            name='storage',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='out_window_goods',
            name='sales',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='out_window_goods',
            name='storage',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='vegetable_goods',
            name='sales',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='vegetable_goods',
            name='storage',
            field=models.TextField(null=True),
        ),
    ]
