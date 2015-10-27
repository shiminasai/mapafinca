# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0004_auto_20151027_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genero4',
            name='respuesta',
        ),
    ]
