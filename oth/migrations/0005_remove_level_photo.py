# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oth', '0004_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='photo',
        ),
    ]
