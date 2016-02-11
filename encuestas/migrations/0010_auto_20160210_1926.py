# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0009_auto_20160127_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimentosfuerafinca',
            name='precio',
            field=models.FloatField(verbose_name=b'Precio unitario en C$'),
        ),
    ]
