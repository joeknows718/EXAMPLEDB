# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_db', '0025_candidate_won_primary'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='candidate',
            options={'ordering': ['last_name']},
        ),
        migrations.AlterModelOptions(
            name='county',
            options={'ordering': ['fips_code']},
        ),
        migrations.AlterModelOptions(
            name='district',
            options={'ordering': ['district_id']},
        ),
        migrations.AlterModelOptions(
            name='election',
            options={'ordering': ['election_name']},
        ),
    ]
