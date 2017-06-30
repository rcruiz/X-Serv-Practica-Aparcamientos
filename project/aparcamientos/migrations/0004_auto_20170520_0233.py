# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0003_auto_20170520_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparcamiento',
            name='email',
            field=models.CharField(default=' ', max_length=128),
        ),
        migrations.AlterField(
            model_name='aparcamiento',
            name='telf',
            field=models.CharField(default=' ', max_length=128),
        ),
    ]
