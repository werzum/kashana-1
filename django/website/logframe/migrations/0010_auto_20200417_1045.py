# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logframe', '0009_auto_20200417_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicator',
            name='question_active',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indicator',
            name='question_category',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='indicator',
            name='question_content',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='subindicator',
            name='question_negative_responses',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='subindicator',
            name='question_number_questionees',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='subindicator',
            name='question_positive_responses',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
