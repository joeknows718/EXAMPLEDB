# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_db', '0007_auto_20160201_2223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='ethnicity',
        ),
        migrations.AddField(
            model_name='candidate',
            name='election',
            field=models.ForeignKey(related_name='candidate', to='pro_db.Election', null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='race',
            field=models.CharField(max_length=100),
        ),
    ]
