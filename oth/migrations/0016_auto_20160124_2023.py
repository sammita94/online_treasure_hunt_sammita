# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oth', '0015_notif'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='photo',
            field=models.ImageField(default=b'static/images/level1.jpg', upload_to=b'static/images/'),
        ),
        migrations.AlterField(
            model_name='notif',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 1, 24, 20, 23, 37, 551813)),
        ),
    ]
