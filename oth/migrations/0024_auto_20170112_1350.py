# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oth', '0023_auto_20170108_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notif',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 1, 12, 13, 50, 55, 377870)),
        ),
    ]
