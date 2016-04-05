# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_db', '0024_auto_20160328_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='won_primary',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No'), (b'Not Sure', b'Not Sure')]),
        ),
    ]
