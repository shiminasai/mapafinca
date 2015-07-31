# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='encuesta',
            name='encuestador',
            field=models.ForeignKey(default=1, to='encuestas.Encuestadores'),
            preserve_default=False,
        ),
    ]
