# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_db', '0016_auto_20160226_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='next_filing_date',
        ),
        migrations.AddField(
            model_name='district',
            name='next_filing_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
