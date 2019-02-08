# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-05 04:42
from __future__ import unicode_literals, absolute_import

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icds_reports', '0089_death_date_in_css_record_monthly_view'),
    ]

    operations = [
        migrations.AddField(
            model_name='aggregatechildhealthdailyfeedingforms',
            name='lunch_count',
            field=models.PositiveSmallIntegerField(help_text='Number of days the child had the lunch', null=True),
        )
    ]
