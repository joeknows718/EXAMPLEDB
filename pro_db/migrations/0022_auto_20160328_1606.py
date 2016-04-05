# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_db', '0021_auto_20160328_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='election_result',
            field=models.URLField(max_length=500, blank=True),
        ),
    ]
