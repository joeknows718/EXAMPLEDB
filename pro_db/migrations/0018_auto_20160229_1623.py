# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_db', '0017_auto_20160229_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='first_year_elected',
            field=models.IntegerField(max_length=4, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='last_year_elected',
            field=models.IntegerField(max_length=4, null=True, blank=True),
        ),
    ]
