# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oth', '0021_auto_20170102_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='accuracy',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='notif',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 1, 3, 22, 3, 47, 292345)),
        ),
    ]
