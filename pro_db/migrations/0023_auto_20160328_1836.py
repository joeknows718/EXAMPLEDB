# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_db', '0022_auto_20160328_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='election_year',
            field=models.IntegerField(default=2000, max_length=4),
        ),
    ]
