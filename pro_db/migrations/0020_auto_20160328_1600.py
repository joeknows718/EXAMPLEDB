# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_db', '0019_auto_20160316_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='election_result',
            field=models.URLField(max_length=255, blank=True),
        ),
    ]
