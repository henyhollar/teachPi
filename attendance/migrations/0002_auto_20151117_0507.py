# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='name',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='reg_no',
        ),
        migrations.AddField(
            model_name='attendance',
            name='present',
            field=models.BooleanField(default=False),
        ),
    ]
