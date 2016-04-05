# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pro_db', '0008_auto_20160203_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='is_appointed',
            field=models.CharField(default=b'Not Sure', max_length=100, choices=[(b'Yes', b'Yes'), (b'No', b'No'), (b'Not Sure', b'Not Sure')]),
        ),
        migrations.AddField(
            model_name='state',
            name='next_filing_date',
            field=models.DateField(default=datetime.datetime(2016, 2, 9, 17, 12, 30, 919363, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='is_incumbent',
            field=models.CharField(default=b'Not Sure', max_length=100, choices=[(b'Yes', b'Yes'), (b'No', b'No'), (b'Not Sure', b'Not Sure')]),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='is_running',
            field=models.CharField(default=b'Not Sure', max_length=100, choices=[(b'Yes', b'Yes'), (b'No', b'No'), (b'Not Sure', b'Not Sure')]),
        ),
        migrations.AlterField(
            model_name='election',
            name='tier',
            field=models.CharField(max_length=2, blank=True),
        ),
    ]
