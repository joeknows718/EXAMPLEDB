# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_db', '0013_auto_20160216_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='election_result',
            field=models.URLField(max_length=150, blank=True),
        ),
        migrations.AlterField(
            model_name='election',
            name='tier',
            field=models.URLField(max_length=2, blank=True),
        ),
    ]
