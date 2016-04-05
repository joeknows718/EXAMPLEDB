# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_db', '0004_auto_20160201_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='election',
            name='election_state',
            field=models.ForeignKey(related_name='election', default='AL', to='pro_db.State'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='party',
            field=models.ForeignKey(related_name='candidate', to='pro_db.Party'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='race',
            field=models.ForeignKey(related_name='candidate', to='pro_db.Election'),
        ),
        migrations.AlterField(
            model_name='district',
            name='state',
            field=models.ForeignKey(related_name='district', to='pro_db.State'),
        ),
        migrations.AlterField(
            model_name='election',
            name='district',
            field=models.ForeignKey(related_name='election', to='pro_db.District'),
        ),
    ]
