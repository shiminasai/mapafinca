# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0006_auto_20151027_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cultivos',
            name='unidad_medida',
            field=models.IntegerField(choices=[(1, b'Quintal'), (2, b'Libras'), (3, b'Docena'), (4, b'Cien'), (5, b'Cabeza'), (6, b'Litro'), (7, b'Unidad')]),
        ),
        migrations.AlterField(
            model_name='cultivosfrutas',
            name='unidad_medida',
            field=models.IntegerField(choices=[(1, b'Quintal'), (2, b'Libras'), (3, b'Docena'), (4, b'Cien'), (5, b'Cabeza'), (6, b'Litro'), (7, b'Unidad')]),
        ),
        migrations.AlterField(
            model_name='cultivoshuertos',
            name='unidad_medida',
            field=models.IntegerField(choices=[(1, b'Quintal'), (2, b'Libras'), (3, b'Docena'), (4, b'Cien'), (5, b'Cabeza'), (6, b'Litro'), (7, b'Unidad')]),
        ),
        migrations.AlterField(
            model_name='entrevistados',
            name='sexo',
            field=models.IntegerField(choices=[(1, b'Mujer'), (2, b'Hombre'), (3, b'Ambos')]),
        ),
        migrations.AlterField(
            model_name='otrasseguridad',
            name='tipo_tratamiento',
            field=models.ForeignKey(blank=True, to='encuestas.TrataAgua', null=True),
        ),
        migrations.AlterField(
            model_name='productoprocesado',
            name='unidad_medida',
            field=models.IntegerField(choices=[(1, b'Quintal'), (2, b'Libras'), (3, b'Docena'), (4, b'Cien'), (5, b'Cabeza'), (6, b'Litro'), (7, b'Unidad')]),
        ),
        migrations.AlterField(
            model_name='respuestano41',
            name='agricola',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=3, null=True, choices=[(b'A', b'Falta de semilla'), (b'B', b'Mala calidad de la semilla')]),
        ),
        migrations.AlterField(
            model_name='respuestano41',
            name='fenomeno',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=7, null=True, choices=[(b'A', b'Sequ\xc3\xada'), (b'B', b'Inundaci\xc3\xb3n'), (b'C', b'Deslizamiento'), (b'D', b'Viento')]),
        ),
        migrations.AlterField(
            model_name='respuestano41',
            name='inversion',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=3, null=True, choices=[(b'A', b'Falta de cr\xc3\xa9dito'), (b'B', b'Alto inter\xc3\xa9s')]),
        ),
        migrations.AlterField(
            model_name='respuestano41',
            name='mercado',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=5, null=True, choices=[(b'A', b'Bajo precio'), (b'B', b'Falta de venta'), (b'C', b'Mala calidad del producto')]),
        ),
        migrations.AlterField(
            model_name='seguridadalimentaria',
            name='misma_finca',
            field=models.IntegerField(null=True, verbose_name=b'34_\xc2\xbfQu\xc3\xa9 porcentaje alimentos que consumen en su hogar provienen de la misma finca?', blank=True),
        ),
        migrations.AlterField(
            model_name='sexomiembros',
            name='sexo',
            field=models.IntegerField(verbose_name=b'7_Quien es el jefe (a) del hogar', choices=[(1, b'Mujer'), (2, b'Hombre'), (3, b'Ambos')]),
        ),
        migrations.AlterField(
            model_name='tratamientoagua',
            name='tratamiento',
            field=models.IntegerField(choices=[(1, b'Se hierve'), (2, b'Se clora'), (3, b'Se usa filtro'), (4, b'Se deja reposar'), (5, b'Sodificaci\xc3\xb3n'), (6, b'Ninguno')]),
        ),
    ]
