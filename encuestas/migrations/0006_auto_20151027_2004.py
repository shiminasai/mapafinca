# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0005_remove_genero4_respuesta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero1',
            name='monto',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
