# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lugar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Microcuenca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=40)),
                ('comunidad', models.ForeignKey(to='lugar.Comunidad')),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Microcuencas',
            },
        ),
    ]
