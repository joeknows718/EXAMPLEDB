# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_db', '0011_auto_20160212_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='slug',
            field=models.SlugField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='district',
            name='slug',
            field=models.SlugField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='election',
            name='slug',
            field=models.SlugField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='state',
            name='slug',
            field=models.SlugField(null=True, blank=True),
        ),
    ]
