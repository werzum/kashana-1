# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logframe', '0008_auto_20160429_1237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='result',
            options={'ordering': ['order']},
        ),
    ]
