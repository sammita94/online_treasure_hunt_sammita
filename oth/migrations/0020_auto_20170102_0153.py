# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oth', '0019_auto_20160124_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='accuracy',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='notif',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 1, 2, 1, 53, 1, 969022)),
        ),
    ]
