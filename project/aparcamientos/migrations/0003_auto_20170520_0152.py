# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0002_auto_20170520_0005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aparcamiento',
            old_name='telefono',
            new_name='telf',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='direccion',
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='dir2',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
    ]
