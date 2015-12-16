# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oth', '0005_remove_level_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='level',
            old_name='number',
            new_name='l_number',
        ),
    ]
