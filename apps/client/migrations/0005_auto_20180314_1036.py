# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-14 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20180314_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='cnpj',
            field=models.FloatField(blank=True, null=True, verbose_name='CNPJ'),
        ),
    ]
