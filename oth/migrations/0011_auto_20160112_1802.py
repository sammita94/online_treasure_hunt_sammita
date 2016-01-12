# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oth', '0010_player_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='timestamp',
            field=models.DateTimeField(default=datetime.time),
        ),
    ]
