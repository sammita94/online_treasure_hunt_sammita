# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oth', '0009_player_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
