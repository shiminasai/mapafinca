# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0002_auto_20150808_0527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='escolaridad',
            name='secu_completa',
        ),
    ]
