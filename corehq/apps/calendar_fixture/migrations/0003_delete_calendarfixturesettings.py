# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-09 12:29
from __future__ import absolute_import, unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_fixture', '0002_auto_20171121_1803'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CalendarFixtureSettings',
        ),
    ]