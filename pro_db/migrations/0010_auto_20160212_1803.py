# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pro_db', '0009_auto_20160209_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='district',
            name='next_election_year',
        ),
        migrations.RemoveField(
            model_name='election',
            name='next_election_date',
        ),
        migrations.AddField(
            model_name='district',
            name='general_election_date',
            field=models.DateField(default=datetime.datetime(2016, 2, 12, 18, 3, 36, 569914, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='district',
            name='primary_election_date',
            field=models.DateField(default=datetime.datetime(2016, 2, 12, 18, 3, 50, 954342, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
