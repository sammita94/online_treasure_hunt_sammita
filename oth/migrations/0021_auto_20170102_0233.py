# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oth', '0020_auto_20170102_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='wrong',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='notif',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 1, 2, 2, 33, 25, 345093)),
        ),
    ]
