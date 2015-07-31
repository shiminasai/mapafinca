# -*- coding: utf-8 -*-
from django.db import models
from lugar.models import *

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
    departameto = models.ForeignKey(Departamento)
    municipio = models.ForeignKey(Municipio)
    comunidad = models.ForeignKey(Comunidad)
    mes = models.IntegerField(choices=CHOICES_MESES)
    year = models.IntegerField('Año')
    precipitacion = models.FloatField()

    total_precipitacion = models.FloatField(editable=False)

    def save(self, *args, **kwargs):
        '''Save sobrecargado para calcular totales'''

        self.total_precipitacion =+ self.precipitacion
        super(Precipitacion, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s-%s-%s' % (str(self.pais),str(self.departameto),str(self.municipio))

    class Media:
        verbose_name='Precipitación'
        verbose_name_plural = 'Precipitación'


class Temperatura(models.Model):
    pais = models.ForeignKey(Pais)
    departameto = models.ForeignKey(Departamento)
    municipio = models.ForeignKey(Municipio)
    comunidad = models.ForeignKey(Comunidad)
    mes = models.IntegerField(choices=CHOICES_MESES)
    year = models.IntegerField('Año')
    temperatura = models.FloatField()

    total_temperatura = models.FloatField(editable=False)

    def save(self, *args, **kwargs):
        '''Save sobrecargado para calcular totales'''

        self.total_temperatura =+ self.temperatura
        super(Temperatura, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s-%s-%s' % (str(self.pais),str(self.departameto),str(self.municipio))

    class Media:
        verbose_name='Temperatura'
        verbose_name_plural = 'Temperatura'

class DiasEfectivoLLuvia(models.Model):
    pais = models.ForeignKey(Pais)
    departameto = models.ForeignKey(Departamento)
    municipio = models.ForeignKey(Municipio)
    comunidad = models.ForeignKey(Comunidad)
    mes = models.IntegerField(choices=CHOICES_MESES)
    year = models.IntegerField('Año')
    dias_lluvia = models.FloatField()

    def __unicode__(self):
        return u'%s-%s-%s' % (str(self.pais),str(self.departameto),str(self.municipio))

    class Media:
        verbose_name='Dias Efectivo de LLuvia'
        verbose_name_plural = 'Dias Efectivo de LLuvia'
