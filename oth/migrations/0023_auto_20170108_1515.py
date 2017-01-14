# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oth', '0022_auto_20170103_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='image',
            field=models.ImageField(default='images/level1.jpg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='notif',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 1, 8, 15, 15, 43, 466057)),
        ),
    ]
