# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entrevistados',
            options={'verbose_name': 'Base de datos Productor', 'verbose_name_plural': 'Base de datos Productores'},
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='org_responsable',
            field=models.ForeignKey(verbose_name=b'Nombre de la organizaci\xc3\xb3n responsable', to='encuestas.OrganizacionResp'),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='year',
            field=models.IntegerField(verbose_name=b'A\xc3\xb1o', editable=False),
        ),
    ]
