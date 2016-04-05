# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_db', '0014_auto_20160225_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='election_result',
            field=models.URLField(max_length=150, blank=True),
        ),
        migrations.AlterField(
            model_name='election',
            name='tier',
            field=models.CharField(max_length=2, blank=True),
        ),
    ]
