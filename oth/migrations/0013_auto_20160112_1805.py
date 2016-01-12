# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oth', '0012_auto_20160112_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
