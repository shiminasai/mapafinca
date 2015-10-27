# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0003_auto_20150817_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.IntegerField(choices=[(1, b'Cultivo tradicionales '), (2, b'Cultivos en huertos familiares '), (3, b'Frutales en finca'), (4, b'Ganader\xc3\xada mayor y menor'), (5, b'Productos procesados'), (6, b'Otras fuentes')])),
                ('porcentaje', models.FloatField(choices=[(1, b'10%'), (2, b'20%'), (3, b'30%'), (4, b'40%'), (5, b'50%'), (6, b'60%'), (7, b'70%'), (8, b'80%'), (9, b'90%'), (10, b'100%')])),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': '43_\xbfQu\xe9 porcentaje de ingreso es aportado por la mujer (compa\xf1era del jefe del hogar)',
            },
        ),
        migrations.CreateModel(
            name='Genero1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.IntegerField(verbose_name=b'44 \xc2\xbfTiene cr\xc3\xa9dito a nombre de la mujer (compa\xc3\xb1era del jefe del hogar)?', choices=[(1, b'Si'), (2, b'No')])),
                ('monto', models.FloatField()),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': '44_\xbfTiene cr\xe9dito a nombre de la mujer (compa\xf1era del jefe del hogar)?',
            },
        ),
        migrations.CreateModel(
            name='Genero2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pregunta', models.IntegerField(choices=[(1, b'Panel solar'), (2, b'Animales (Ganado mayor o menor)'), (3, b'Equipos de producci\xc3\xb3n')])),
                ('respuesta', models.IntegerField(choices=[(1, b'Si'), (2, b'No')])),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': '45_\xbfTiene a nombre de la mujer (compa\xf1era del jefe del hogar) algunos de los siguientes bienes?',
            },
        ),
        migrations.CreateModel(
            name='Genero3',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('respuesta', models.IntegerField(verbose_name=b'\xc2\xbfLa mujer (compa\xc3\xb1era del jefe del hogar) pertenece a alg\xc3\xban tipo de organizaci\xc3\xb3n?', choices=[(1, b'Si'), (2, b'No')])),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': '46_\xbfLa mujer (compa\xf1era del jefe del hogar) pertenece a alg\xfan tipo de organizaci\xf3n ?',
            },
        ),
        migrations.CreateModel(
            name='Genero4',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('opcion', models.IntegerField(verbose_name=b'\xc2\xbfnivel de educaci\xc3\xb3n de la mujer (compa\xc3\xb1era del jefe del hogar)?', choices=[(1, b'No lee, ni escribe'), (2, b'Primaria incompleta'), (3, b'Primaria completa'), (4, b'Secundaria incompleta'), (5, b'Bachiller'), (6, b'Universitario o t\xc3\xa9cnico')])),
                ('respuesta', models.IntegerField(choices=[(1, b'Si'), (2, b'No')])),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': '47_\xbfCu\xe1l es el nivel de educaci\xf3n de la mujer (compa\xf1era del jefe del hogar)',
            },
        ),
        migrations.AlterModelOptions(
            name='alimentosfuerafinca',
            options={'verbose_name_plural': '42_Indique los alimentos que compra fuera de la finca'},
        ),
        migrations.AlterModelOptions(
            name='respuestano41',
            options={'verbose_name_plural': '40.1_Si responde NO'},
        ),
        migrations.RemoveField(
            model_name='seguridadalimentaria',
            name='fuera_finca',
        ),
        migrations.AddField(
            model_name='panelsolar',
            name='si_no',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'Si'), (2, b'No')]),
        ),
        migrations.AddField(
            model_name='procesamiento',
            name='cantidad_total',
            field=models.FloatField(null=True, verbose_name=b'Cantidad', blank=True),
        ),
        migrations.AddField(
            model_name='productoprocesado',
            name='codigo',
            field=models.CharField(max_length=4, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='otrasseguridad',
            name='adquiere_agua',
            field=models.ForeignKey(verbose_name=b'41_En momentos de sequ\xc3\xada como adquiere el agua de consumo', to='encuestas.AdquiereAgua'),
        ),
        migrations.AlterField(
            model_name='otrasseguridad',
            name='tratamiento',
            field=models.IntegerField(verbose_name=b'41_1 Le da alg\xc3\xban tipo de tratamiento:', choices=[(1, b'Si'), (2, b'No')]),
        ),
        migrations.AlterField(
            model_name='practicasagroecologicas',
            name='control',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'33_\xc2\xbfRealiza control y monitoreo de plagas y enfermedades?', choices=[(1, b'Si'), (2, b'No')]),
        ),
        migrations.AlterField(
            model_name='practicasagroecologicas',
            name='fertilidad',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'32_\xc2\xbfRealizan an\xc3\xa1lisis de fertilidad del suelo?', choices=[(1, b'Si'), (2, b'No')]),
        ),
        migrations.AlterField(
            model_name='practicasagroecologicas',
            name='manejo',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'30_Sobre el manejo del suelo \xc2\xbfC\xc3\xb3mo preparan el suelo?', choices=[(1, b'Tala y quema'), (2, b'Trabaja en crudo'), (3, b'Arado'), (4, b'Uso de cobertura')]),
        ),
        migrations.AlterField(
            model_name='practicasagroecologicas',
            name='traccion',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'31_\xc2\xbfQu\xc3\xa9 tipo de tracci\xc3\xb3n utilizan para la preparaci\xc3\xb3n del suelo?', choices=[(1, b'Animal'), (2, b'Humana'), (3, b'Tractor'), (4, b'Ninguna')]),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='algun_prestamo',
            field=models.IntegerField(verbose_name=b'En el \xc3\xbaltimo a\xc3\xb1o ha recibido alg\xc3\xban tipo de prestamo/cr\xc3\xa9dito', choices=[(1, b'Si'), (2, b'No')]),
        ),
        migrations.AlterField(
            model_name='seguridadalimentaria',
            name='ayuda',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'38_\xc2\xbfCuentan con ayuda de alimentos en momentos de escasez?', choices=[(1, b'Si'), (2, b'No')]),
        ),
        migrations.AlterField(
            model_name='seguridadalimentaria',
            name='consumo_diario',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'40_\xc2\xbfConsidera que su familia cuenta con la cantidad necesaria de alimentos que necesitan para el consumo diario del hogar?', choices=[(1, b'Si'), (2, b'No')]),
        ),
        migrations.AlterField(
            model_name='seguridadalimentaria',
            name='economico',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'35_\xc2\xbfDisponen suficiente recursos econ\xc3\xb3micos para manejo de finca?', choices=[(1, b'Si'), (2, b'No')]),
        ),
        migrations.AlterField(
            model_name='seguridadalimentaria',
            name='misma_finca',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'34_\xc2\xbfQu\xc3\xa9 porcentaje alimentos que consumen en su hogar provienen de la misma finca?', choices=[(1, b'10%'), (2, b'20%'), (3, b'30%'), (4, b'40%'), (5, b'50%'), (6, b'60%'), (7, b'70%'), (8, b'80%'), (9, b'90%'), (10, b'100%')]),
        ),
        migrations.AlterField(
            model_name='seguridadalimentaria',
            name='plan_cosecha',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'37_\xc2\xbfCuentan con un plan de cosecha?', choices=[(1, b'Si'), (2, b'No')]),
        ),
        migrations.AlterField(
            model_name='seguridadalimentaria',
            name='secado',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'36_\xc2\xbfDispone de tecnolog\xc3\xada para el secado y almacenamiento de cosecha?', choices=[(1, b'Si'), (2, b'No')]),
        ),
        migrations.AlterField(
            model_name='seguridadalimentaria',
            name='suficiente_alimento',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'39_\xc2\xbfLe ha preocupado que en su hogar no hubiera suficiente alimentos?', choices=[(1, b'Si'), (2, b'No')]),
        ),
    ]
