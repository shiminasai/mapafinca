# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


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
                ('departamento', models.ForeignKey(to='lugar.Departamento')),
                ('municipio', models.ForeignKey(to='lugar.Municipio')),
                ('pais', models.ForeignKey(to='lugar.Pais')),
            ],
            options={
                'verbose_name': 'Dias Efectivo de LLuvia',
                'verbose_name_plural': 'Dias Efectivo de LLuvia',
            },
        ),
        migrations.CreateModel(
            name='Precipitacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mes', models.IntegerField(choices=[(1, b'Enero'), (2, b'Febrero'), (3, b'Marzo'), (4, b'Abril'), (5, b'Mayo'), (6, b'Junio'), (7, b'Julio'), (8, b'Agosto'), (9, b'Septiembre'), (10, b'Octubre'), (11, b'Noviembre'), (12, b'Diciembre')])),
                ('year', models.IntegerField(verbose_name=b'A\xc3\xb1o')),
                ('precipitacion', models.FloatField()),
                ('total_precipitacion', models.FloatField(editable=False)),
                ('comunidad', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'municipio', chained_field=b'municipio', blank=True, auto_choose=True, to='lugar.Comunidad', null=True)),
                ('departamento', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'pais', chained_field=b'pais', auto_choose=True, to='lugar.Departamento')),
                ('municipio', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'departamento', chained_field=b'departamento', auto_choose=True, to='lugar.Municipio')),
                ('pais', models.ForeignKey(to='lugar.Pais')),
            ],
            options={
                'verbose_name': 'Precipitaci\xf3n',
                'verbose_name_plural': 'Precipitaci\xf3n',
            },
        ),
        migrations.CreateModel(
            name='Temperatura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mes', models.IntegerField(choices=[(1, b'Enero'), (2, b'Febrero'), (3, b'Marzo'), (4, b'Abril'), (5, b'Mayo'), (6, b'Junio'), (7, b'Julio'), (8, b'Agosto'), (9, b'Septiembre'), (10, b'Octubre'), (11, b'Noviembre'), (12, b'Diciembre')])),
                ('year', models.IntegerField(verbose_name=b'A\xc3\xb1o')),
                ('temperatura', models.FloatField()),
                ('total_temperatura', models.FloatField(editable=False)),
                ('comunidad', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'municipio', chained_field=b'municipio', blank=True, auto_choose=True, to='lugar.Comunidad', null=True)),
                ('departamento', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'pais', chained_field=b'pais', auto_choose=True, to='lugar.Departamento')),
                ('municipio', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'departamento', chained_field=b'departamento', auto_choose=True, to='lugar.Municipio')),
                ('pais', models.ForeignKey(to='lugar.Pais')),
            ],
            options={
                'verbose_name': 'Temperatura',
                'verbose_name_plural': 'Temperatura',
            },
        ),
    ]
