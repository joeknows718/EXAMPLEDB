# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_db', '0020_auto_20160328_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='percent_aa',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='district',
            name='percent_latino',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='district',
            name='percent_obama',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='district',
            name='population',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]
