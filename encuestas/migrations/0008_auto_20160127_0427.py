# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0007_auto_20151028_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='cultivos',
            name='calorias',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cultivos',
            name='proteinas',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cultivosfrutas',
            name='calorias',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cultivosfrutas',
            name='proteinas',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cultivoshuertos',
            name='calorias',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cultivoshuertos',
            name='proteinas',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='productoprocesado',
            name='calorias',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='productoprocesado',
            name='proteinas',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
