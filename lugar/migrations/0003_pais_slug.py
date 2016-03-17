# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lugar', '0002_microcuenca'),
    ]

    operations = [
        migrations.AddField(
            model_name='pais',
            name='slug',
            field=models.SlugField(help_text=b'Usado como url unica(autorellenado)', unique=True, null=True),
        ),
    ]
