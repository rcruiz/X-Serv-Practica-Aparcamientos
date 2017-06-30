# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0004_auto_20170520_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparcamiento',
            name='email',
            field=models.CharField(max_length=128, default=''),
        ),
        migrations.AlterField(
            model_name='aparcamiento',
            name='telf',
            field=models.CharField(max_length=64, default=''),
        ),
    ]
