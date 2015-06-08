# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lugar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleMiembros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('edad', models.IntegerField(choices=[(1, b'Hombres > 31 a\xc3\xb1os'), (2, b'Mujeres > 31 a\xc3\xb1os'), (3, b'Ancianos > 64 a\xc3\xb1os'), (4, b'Ancianas > 64 a\xc3\xb1os'), (5, b'Mujer joven de 19 a 30 a\xc3\xb1os'), (6, b'Hombre joven de 19 a 30 a\xc3\xb1os'), (7, b'Mujer adolescente 13 a 18 a\xc3\xb1os'), (8, b'Hombre adolescente 13 a 18 a\xc3\xb1os'), (9, b'Ni\xc3\xb1as 5 a 12 a\xc3\xb1os'), (10, b'Ni\xc3\xb1os 5 a 12 a\xc3\xb1os '), (11, b'Ni\xc3\xb1as 0 a 4 a\xc3\xb1os '), (12, b'Ni\xc3\xb1os 0 a 4 a\xc3\xb1os')])),
                ('cantidad', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': '9_Detalle la cantidad de miembros del hogar seg\xfan edad y sexo',
            },
        ),
        migrations.CreateModel(
            name='DuenoNo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('no', models.IntegerField(choices=[(1, b'Arrendada'), (2, b'Promesa de venta'), (3, b'Prestada'), (4, b'Tierra Ind\xc3\xadgena'), (5, b'Sin escritura'), (6, b'Colectivo/Cooperativa')])),
            ],
            options={
                'verbose_name_plural': '6.2_En el caso que diga NO, especifique la situaci\xf3n',
            },
        ),
        migrations.CreateModel(
            name='DuenoSi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('si', models.IntegerField(choices=[(1, b'A nombre del hombre'), (2, b'A nombre de la mujer'), (3, b'A nombre de los hijos'), (4, b'Mancomunado')])),
            ],
            options={
                'verbose_name_plural': '6.1_En el caso SI, indique a nombre de quien est\xe1',
            },
        ),
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('dueno', models.IntegerField(verbose_name=b'\xc2\xbfSon due\xc3\xb1os de la propiedad/finca?', choices=[(1, b'Si'), (2, b'No')])),
                ('year', models.IntegerField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Encuestadores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Encuestador',
                'verbose_name_plural': 'Encuestadores',
            },
        ),
        migrations.CreateModel(
            name='Entrevistados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250, verbose_name=b'Nombre Completo')),
                ('cedula', models.CharField(max_length=50, verbose_name=b'No. C\xc3\xa9dula')),
                ('ocupacion', models.CharField(max_length=150, verbose_name=b'Ocupaci\xc3\xb3n')),
                ('sexo', models.IntegerField(choices=[(1, b'Mujer'), (2, b'Hombre')])),
                ('jefe', models.IntegerField(verbose_name=b'Jefe del hogar', choices=[(1, b'Si'), (2, b'No')])),
                ('edad', models.IntegerField()),
                ('latitud', models.FloatField(blank=True)),
                ('longitud', models.FloatField(blank=True)),
                ('finca', models.CharField(max_length=250, verbose_name=b'Nombre de la finca')),
                ('comunidad', models.ForeignKey(to='lugar.Comunidad')),
                ('departamento', models.ForeignKey(to='lugar.Departamento')),
                ('municipio', models.ForeignKey(to='lugar.Municipio')),
                ('pais', models.ForeignKey(to='lugar.Pais')),
            ],
            options={
                'verbose_name': 'Entrevistado',
                'verbose_name_plural': 'Entrevistados',
            },
        ),
        migrations.CreateModel(
            name='Escolaridad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sexo', models.IntegerField(choices=[(1, b'Hombres mayores 31 a\xc3\xb1os'), (2, b'Mujeres mayores 31 a\xc3\xb1os'), (3, b'Hombre joven de 19 a 30 a\xc3\xb1os'), (4, b'Mujer joven de 19 a 30 a\xc3\xb1os'), (5, b'Hombre adolescente 13 a 18 a\xc3\xb1os'), (6, b'Mujer adolescente 13 a 18 a\xc3\xb1os'), (7, b'Ni\xc3\xb1os 5 a 12 a\xc3\xb1os'), (8, b'Ni\xc3\xb1as 5 a 12 a\xc3\xb1os ')])),
                ('no_leer', models.IntegerField(verbose_name=b'No lee,ni escribe')),
                ('pri_incompleta', models.IntegerField(verbose_name=b'Primaria incompleta')),
                ('pri_completa', models.IntegerField(verbose_name=b'Primaria completa')),
                ('secu_incompleta', models.IntegerField(verbose_name=b'Secundaria incompleta')),
                ('secu_completa', models.IntegerField(verbose_name=b'Secundaria completa')),
                ('bachiller', models.IntegerField(verbose_name=b'Bachiller')),
                ('uni_tecnico', models.IntegerField(verbose_name=b'Universitario o t\xc3\xa9cnico')),
                ('total', models.IntegerField(verbose_name=b'total')),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': '10_Nivel de escolaridad (n\xfamero por categor\xeda)',
            },
        ),
        migrations.CreateModel(
            name='OrganizacionResp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Organizaci\xf3n responsable',
                'verbose_name_plural': 'Organizaciones responsables',
            },
        ),
        migrations.CreateModel(
            name='SexoMiembros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sexo', models.IntegerField(verbose_name=b'7_Sexo del jefe (a) del hogar', choices=[(1, b'Mujer'), (2, b'Hombre')])),
                ('cantidad', models.IntegerField(verbose_name=b'8_Cantidad de personas que habitan en el hogar')),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': 'Sexo del jefe del hogar y cantidad de miembros',
            },
        ),
        migrations.AddField(
            model_name='encuesta',
            name='entrevistado',
            field=models.ForeignKey(to='encuestas.Entrevistados'),
        ),
        migrations.AddField(
            model_name='duenosi',
            name='encuesta',
            field=models.ForeignKey(to='encuestas.Encuesta'),
        ),
        migrations.AddField(
            model_name='duenono',
            name='encuesta',
            field=models.ForeignKey(to='encuestas.Encuesta'),
        ),
        migrations.AddField(
            model_name='detallemiembros',
            name='encuesta',
            field=models.ForeignKey(to='encuestas.Encuesta'),
        ),
    ]
