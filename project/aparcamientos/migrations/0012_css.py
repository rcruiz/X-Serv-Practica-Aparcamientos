# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0011_auto_20170525_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Css',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('usuario', models.CharField(max_length=32)),
                ('tamLetra', models.IntegerField()),
                ('colorFondo', models.CharField(max_length=32)),
                ('titulo', models.CharField(max_length=128)),
            ],
        ),
    ]
