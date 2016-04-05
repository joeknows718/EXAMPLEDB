# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_db', '0002_state_notes2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='notes2',
        ),
    ]
