# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-11 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0022_auto_20180829_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='year_of_graduation',
            field=models.IntegerField(choices=[(2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028)], default=2019, verbose_name='year'),
        ),
    ]
