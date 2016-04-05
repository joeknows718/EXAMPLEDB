# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_db', '0015_auto_20160225_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='general_election_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='district',
            name='primary_election_date',
            field=models.DateField(null=True),
        ),
    ]
