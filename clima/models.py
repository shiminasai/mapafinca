# -*- coding: utf-8 -*-
from django.db import models
from lugar.models import *
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.

CHOICES_MESES = (
                    (1, 'Enero'),
                    (2, 'Febrero'),
                    (3, 'Marzo'),
                    (4, 'Abril'),
                    (5, 'Mayo'),
                    (6, 'Junio'),
                    (7, 'Julio'),
                    (8, 'Agosto'),
                    (9, 'Septiembre'),
                    (10, 'Octubre'),
                    (11, 'Noviembre'),
                    (12, 'Diciembre'),
                )

class Precipitacion(models.Model):
    pais = models.ForeignKey(Pais)
    departamento = ChainedForeignKey(
        Departamento,
        chained_field="pais",
        chained_model_field="pais",
        show_all=False,
        auto_choose=True
    )
    municipio = ChainedForeignKey(
        Municipio,
        chained_field="departamento",
        chained_model_field="departamento",
        show_all=False,
        auto_choose=True
    )
    comunidad = ChainedForeignKey(
        Comunidad,
        chained_field="municipio",
        chained_model_field="municipio",
        show_all=False,
        auto_choose=True,
        null=True,
        blank=True,
    )
    mes = models.IntegerField(choices=CHOICES_MESES)
    year = models.IntegerField('Año')
    precipitacion = models.FloatField()

    total_precipitacion = models.FloatField(editable=False)

    def save(self, *args, **kwargs):
        '''Save sobrecargado para calcular totales'''

        self.total_precipitacion =+ self.precipitacion
        super(Precipitacion, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s' % (str(self.precipitacion))

    class Meta:
        verbose_name = 'Precipitación'
        verbose_name_plural = 'Precipitación'


class Temperatura(models.Model):
    pais = models.ForeignKey(Pais)
    departamento = ChainedForeignKey(
        Departamento,
        chained_field="pais",
        chained_model_field="pais",
        show_all=False,
        auto_choose=True
    )
    municipio = ChainedForeignKey(
        Municipio,
        chained_field="departamento",
        chained_model_field="departamento",
        show_all=False,
        auto_choose=True
    )
    comunidad = ChainedForeignKey(
        Comunidad,
        chained_field="municipio",
        chained_model_field="municipio",
        show_all=False,
        auto_choose=True,
        null=True,
        blank=True,
    )
    mes = models.IntegerField(choices=CHOICES_MESES)
    year = models.IntegerField('Año')
    temperatura = models.FloatField()

    total_temperatura = models.FloatField(editable=False)

    def save(self, *args, **kwargs):
        '''Save sobrecargado para calcular totales'''

        self.total_temperatura =+ self.temperatura
        super(Temperatura, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s-%s-%s' % (str(self.pais),str(self.departamento),str(self.municipio))

    class Meta:
        verbose_name='Temperatura'
        verbose_name_plural = 'Temperatura'

class DiasEfectivoLLuvia(models.Model):
    pais = models.ForeignKey(Pais)
    departamento = models.ForeignKey(Departamento)
    municipio = models.ForeignKey(Municipio)
    comunidad = models.ForeignKey(Comunidad)
    mes = models.IntegerField(choices=CHOICES_MESES)
    year = models.IntegerField('Año')
    dias_lluvia = models.FloatField()

    def __unicode__(self):
        return u'%s-%s-%s' % (str(self.pais),str(self.departamento),str(self.municipio))

    class Meta:
        verbose_name='Dias Efectivo de LLuvia'
        verbose_name_plural = 'Dias Efectivo de LLuvia'
