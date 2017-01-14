# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oth', '0025_auto_20170113_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notif',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 1, 13, 22, 49, 48, 930265)),
        ),
    ]
