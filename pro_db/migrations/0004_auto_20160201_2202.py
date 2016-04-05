# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_db', '0003_remove_state_notes2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='district',
            old_name='election_year',
            new_name='next_election_year',
        ),
        migrations.AlterField(
            model_name='district',
            name='percent_aa',
            field=models.DecimalField(max_digits=4, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='district',
            name='percent_latino',
            field=models.DecimalField(max_digits=4, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='district',
            name='percent_obama',
            field=models.DecimalField(max_digits=4, decimal_places=2, blank=True),
        ),
    ]
