# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import json_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('form_processor', '0047_add_deleted_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='caseattachmentsql',
            name='attachment_from',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='caseattachmentsql',
            name='attachment_properties',
            field=json_field.fields.JSONField(default=dict, help_text='Enter a valid JSON object'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='caseattachmentsql',
            name='attachment_size',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='caseattachmentsql',
            name='attachment_src',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='caseattachmentsql',
            name='identifier',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='caseattachmentsql',
            name='server_mime',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
    ]
