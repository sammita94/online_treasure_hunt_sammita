# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oth', '0018_auto_20160124_2116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='level',
            old_name='photo',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='notif',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 1, 24, 21, 50, 36, 191875)),
        ),
    ]
