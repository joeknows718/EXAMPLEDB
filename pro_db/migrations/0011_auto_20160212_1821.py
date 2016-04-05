# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_db', '0010_auto_20160212_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='election_result',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='organization',
            field=models.CharField(max_length=144, blank=True),
        ),
    ]
