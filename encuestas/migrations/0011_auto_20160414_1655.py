# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lugar', '0003_pais_slug'),
        ('encuestas', '0010_auto_20160210_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizacionresp',
            name='departamento',
            field=models.ForeignKey(to='lugar.Departamento', null=True),
        ),
        migrations.AddField(
            model_name='organizacionresp',
            name='municipio',
            field=models.ForeignKey(to='lugar.Municipio', null=True),
        ),
        migrations.AddField(
            model_name='organizacionresp',
            name='pais',
            field=models.ForeignKey(to='lugar.Pais', null=True),
        ),
        migrations.AlterField(
            model_name='respuestano41',
            name='inversion',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=3, null=True, choices=[(b'A', b'Falta de cr\xc3\xa9dito'), (b'B', b'Intereses altos')]),
        ),
    ]
