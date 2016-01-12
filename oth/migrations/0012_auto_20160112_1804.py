# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oth', '0011_auto_20160112_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 12, 18, 4, 12, 742281)),
        ),
    ]
