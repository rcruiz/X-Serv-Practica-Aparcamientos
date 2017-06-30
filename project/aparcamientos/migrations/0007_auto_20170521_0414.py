# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0006_auto_20170520_0254'),
    ]

    operations = [
        migrations.AddField(
            model_name='aparcamiento',
            name='ncomment',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='aparcamiento',
            name='email',
            field=models.CharField(default='', max_length=128),
        ),
    ]
