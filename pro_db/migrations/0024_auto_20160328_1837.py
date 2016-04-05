# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_db', '0023_auto_20160328_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='election_year',
            field=models.IntegerField(max_length=4, null=True, blank=True),
        ),
    ]
