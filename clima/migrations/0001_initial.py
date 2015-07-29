# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lugar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiasEfectivoLLuvia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mes', models.IntegerField(choices=[(1, b'Enero'), (2, b'Febrero'), (3, b'Marzo'), (4, b'Abril'), (5, b'Mayo'), (6, b'Junio'), (7, b'Julio'), (8, b'Agosto'), (9, b'Septiembre'), (10, b'Octubre'), (11, b'Noviembre'), (12, b'Diciembre')])),
                ('year', models.IntegerField(verbose_name=b'A\xc3\xb1o')),
                ('dias_lluvia', models.FloatField()),
                ('comunidad', models.ForeignKey(to='lugar.Comunidad')),
                ('departameto', models.ForeignKey(to='lugar.Departamento')),
                ('municipio', models.ForeignKey(to='lugar.Municipio')),
                ('pais', models.ForeignKey(to='lugar.Pais')),
            ],
        ),
        migrations.CreateModel(
            name='Precipitacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mes', models.IntegerField(choices=[(1, b'Enero'), (2, b'Febrero'), (3, b'Marzo'), (4, b'Abril'), (5, b'Mayo'), (6, b'Junio'), (7, b'Julio'), (8, b'Agosto'), (9, b'Septiembre'), (10, b'Octubre'), (11, b'Noviembre'), (12, b'Diciembre')])),
                ('year', models.IntegerField(verbose_name=b'A\xc3\xb1o')),
                ('precipitacion', models.FloatField()),
                ('total_precipitacion', models.FloatField()),
                ('comunidad', models.ForeignKey(to='lugar.Comunidad')),
                ('departameto', models.ForeignKey(to='lugar.Departamento')),
                ('municipio', models.ForeignKey(to='lugar.Municipio')),
                ('pais', models.ForeignKey(to='lugar.Pais')),
            ],
        ),
        migrations.CreateModel(
            name='Temperatura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mes', models.IntegerField(choices=[(1, b'Enero'), (2, b'Febrero'), (3, b'Marzo'), (4, b'Abril'), (5, b'Mayo'), (6, b'Junio'), (7, b'Julio'), (8, b'Agosto'), (9, b'Septiembre'), (10, b'Octubre'), (11, b'Noviembre'), (12, b'Diciembre')])),
                ('year', models.IntegerField(verbose_name=b'A\xc3\xb1o')),
                ('temperatura', models.FloatField()),
                ('total_temperatura', models.FloatField()),
                ('comunidad', models.ForeignKey(to='lugar.Comunidad')),
                ('departameto', models.ForeignKey(to='lugar.Departamento')),
                ('municipio', models.ForeignKey(to='lugar.Municipio')),
                ('pais', models.ForeignKey(to='lugar.Pais')),
            ],
        ),
    ]
