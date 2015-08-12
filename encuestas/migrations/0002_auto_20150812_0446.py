# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='introducidoshuertos',
            name='cultivo',
            field=models.ForeignKey(verbose_name=b'Cultivos en huertos familiares', to='encuestas.CultivosHuertos'),
        ),
    ]
