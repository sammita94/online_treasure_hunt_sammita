# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oth', '0006_auto_20151216_1142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='college',
        ),
        migrations.RemoveField(
            model_name='player',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='player',
            name='max_level',
            field=models.IntegerField(default=1),
        ),
    ]
