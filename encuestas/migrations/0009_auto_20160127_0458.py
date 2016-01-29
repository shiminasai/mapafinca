# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0008_auto_20160127_0427'),
    ]

    operations = [
        migrations.AddField(
            model_name='productosfuerafinca',
            name='calorias',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='productosfuerafinca',
            name='proteinas',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
