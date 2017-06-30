# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0008_auto_20170522_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparcaseleccionado',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]
