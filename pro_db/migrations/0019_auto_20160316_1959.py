# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_db', '0018_auto_20160229_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='gender',
            field=models.CharField(default=b'Not Sure', max_length=100, choices=[(b'M', b'M'), (b'F', b'F'), (b'Not Sure', b'Not Sure')]),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='race',
            field=models.CharField(default=b'Not Sure', max_length=100),
        ),
    ]
