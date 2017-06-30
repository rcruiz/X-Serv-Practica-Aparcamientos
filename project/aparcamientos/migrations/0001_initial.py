# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aparcamiento',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('direccion', models.CharField(max_length=256)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('descripcion', models.TextField()),
                ('accesible', models.BooleanField(default=False)),
                ('barrio', models.CharField(max_length=64)),
                ('distrito', models.CharField(max_length=32)),
                ('email', models.CharField(default='', max_length=128)),
                ('telefono', models.CharField(default='', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='AparcaSeleccionado',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('fecha', models.DateField(auto_now=True)),
                ('usuario', models.CharField(max_length=32)),
                ('aparcamiento', models.ForeignKey(to='aparcamientos.Aparcamiento')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('contenido', models.TextField(default='')),
                ('aparcamiento', models.ForeignKey(to='aparcamientos.Aparcamiento')),
            ],
        ),
    ]
