# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0002_auto_20150812_0446'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostoFrutas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_mz', models.FloatField(verbose_name=b'\xc3\x81rea Total en Mz')),
                ('costo', models.FloatField(verbose_name=b'Costo total en C$')),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': 'Total Mz y costo para huerto familiar',
            },
        ),
        migrations.CreateModel(
            name='CostoHuerto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_mz', models.FloatField(verbose_name=b'\xc3\x81rea Total en Mz')),
                ('costo', models.FloatField(verbose_name=b'Costo total en C$')),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': 'Total Mz y costo para huerto familiar',
            },
        ),
        migrations.RemoveField(
            model_name='cultivosfrutasfinca',
            name='costo',
        ),
        migrations.RemoveField(
            model_name='cultivoshuertosfamiliares',
            name='costo',
        ),
        migrations.AlterField(
            model_name='ganaderia',
            name='cantidad_vendida',
            field=models.IntegerField(null=True, verbose_name=b'Cantidad vendida este a\xc3\xb1o', blank=True),
        ),
        migrations.AlterField(
            model_name='ganaderia',
            name='mercado',
            field=models.ForeignKey(blank=True, to='encuestas.TipoMercado', null=True),
        ),
        migrations.AlterField(
            model_name='ganaderia',
            name='precio',
            field=models.FloatField(null=True, verbose_name=b'Precio de venta en C$', blank=True),
        ),
        migrations.AlterField(
            model_name='ganaderia',
            name='si_no',
            field=models.IntegerField(verbose_name=b'Comercializa SI/NO', choices=[(1, b'Si'), (2, b'No')]),
        ),
        migrations.AlterField(
            model_name='ganaderia',
            name='total',
            field=models.FloatField(null=True, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='introducidoshuertos',
            name='si_no',
            field=models.IntegerField(verbose_name=b'El dedicarse a cultivar ese cultivo es porque el progama lo ha promovido', choices=[(1, b'Si'), (2, b'No')]),
        ),
        migrations.AlterField(
            model_name='introducidostradicionales',
            name='si_no',
            field=models.IntegerField(verbose_name=b'El dedicarse a cultivar ese cultivo es porque el progama lo ha promovido', choices=[(1, b'Si'), (2, b'No')]),
        ),
        migrations.AlterField(
            model_name='procesamiento',
            name='cantidad',
            field=models.IntegerField(verbose_name=b'Cantidad consumida en el hogar'),
        ),
        migrations.AlterField(
            model_name='respuestano41',
            name='agricola',
            field=multiselectfield.db.fields.MultiSelectField(max_length=3, choices=[(b'A', b'Falta de semilla'), (b'B', b'Mala calidad de la semilla')]),
        ),
        migrations.AlterField(
            model_name='respuestano41',
            name='fenomeno',
            field=multiselectfield.db.fields.MultiSelectField(max_length=7, choices=[(b'A', b'Sequ\xc3\xada'), (b'B', b'Inundaci\xc3\xb3n'), (b'C', b'Deslizamiento'), (b'D', b'Viento')]),
        ),
        migrations.AlterField(
            model_name='respuestano41',
            name='inversion',
            field=multiselectfield.db.fields.MultiSelectField(max_length=3, choices=[(b'A', b'Falta de cr\xc3\xa9dito'), (b'B', b'Alto inter\xc3\xa9s')]),
        ),
        migrations.AlterField(
            model_name='respuestano41',
            name='mercado',
            field=multiselectfield.db.fields.MultiSelectField(max_length=5, choices=[(b'A', b'Bajo precio'), (b'B', b'Falta de venta'), (b'C', b'Mala calidad del producto')]),
        ),
        migrations.AlterField(
            model_name='seguridadalimentaria',
            name='ayuda',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'39_\xc2\xbfCuentan con ayuda de alimentos en momentos de escasez?', choices=[(1, b'Si'), (2, b'No')]),
        ),
        migrations.AlterField(
            model_name='seguridadalimentaria',
            name='consumo_diario',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'41_\xc2\xbfConsidera que su familia cuenta con la cantidad necesaria de alimentos que necesitan para el consumo diario del hogar?', choices=[(1, b'Si'), (2, b'No')]),
        ),
        migrations.AlterField(
            model_name='seguridadalimentaria',
            name='economico',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'36_\xc2\xbfDisponen suficiente recursos econ\xc3\xb3micos para manejo de finca?', choices=[(1, b'Si'), (2, b'No')]),
        ),
        migrations.AlterField(
            model_name='seguridadalimentaria',
            name='fuera_finca',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'35.2_\xc2\xbfQu\xc3\xa9 porcentaje alimentos que consumen en su hogar provienen fuera de la finca?', choices=[(1, b'10%'), (2, b'20%'), (3, b'30%'), (4, b'40%'), (5, b'50%'), (6, b'60%'), (7, b'70%'), (8, b'80%'), (9, b'90%'), (10, b'100%')]),
        ),
        migrations.AlterField(
            model_name='seguridadalimentaria',
            name='misma_finca',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'35.1_\xc2\xbfQu\xc3\xa9 porcentaje alimentos que consumen en su hogar provienen de la misma finca?', choices=[(1, b'10%'), (2, b'20%'), (3, b'30%'), (4, b'40%'), (5, b'50%'), (6, b'60%'), (7, b'70%'), (8, b'80%'), (9, b'90%'), (10, b'100%')]),
        ),
        migrations.AlterField(
            model_name='seguridadalimentaria',
            name='plan_cosecha',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'38_\xc2\xbfCuentan con un plan de cosecha?', choices=[(1, b'Si'), (2, b'No')]),
        ),
        migrations.AlterField(
            model_name='seguridadalimentaria',
            name='secado',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'37_\xc2\xbfDispone de tecnolog\xc3\xada para el secado y almacenamiento de cosecha?', choices=[(1, b'Si'), (2, b'No')]),
        ),
        migrations.AlterField(
            model_name='seguridadalimentaria',
            name='suficiente_alimento',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'40_\xc2\xbfLe ha preocupado que en su hogar no hubiera suficiente alimentos?', choices=[(1, b'Si'), (2, b'No')]),
        ),
        migrations.AlterField(
            model_name='seguridadalimentaria',
            name='tipo_secado',
            field=models.ForeignKey(verbose_name=b'Si es si cu\xc3\xa1l?', blank=True, to='encuestas.TipoSecado', null=True),
        ),
    ]
