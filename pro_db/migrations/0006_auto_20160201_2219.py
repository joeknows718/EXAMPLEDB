# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_db', '0005_auto_20160201_2216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='election',
            old_name='election_state',
            new_name='state',
        ),
    ]
