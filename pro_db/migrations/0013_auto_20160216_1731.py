# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_db', '0012_auto_20160216_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='next_filing_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
