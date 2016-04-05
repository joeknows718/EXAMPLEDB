# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_db', '0006_auto_20160201_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='percent_vote',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
