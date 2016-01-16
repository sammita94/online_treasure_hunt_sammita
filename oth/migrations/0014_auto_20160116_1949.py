# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oth', '0013_auto_20160112_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
