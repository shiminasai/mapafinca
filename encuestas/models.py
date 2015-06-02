# -*- coding: utf-8 -*-
from django.db import models
from lugar.models import Pais, Departamento, Municipio, Comunidad
# Create your models here.
#CHOICES ESTATICOS
CHOICE_SEXO = (
                (1, 'Mujer'),
                (2, 'Hombre'),
              )
CHOICE_JEFE = (
                (1, 'Si'),
                (2, 'No'),
              )
CHOICE_DUENO_SI = (
                (1, 'A nombre del hombre'),
                (2, 'A nombre de la mujer'),
                (3, 'A nombre de los hijos'),
                (4, 'Mancomunado'),
              )
CHOICE_DUENO_NO = (
                (1, 'Arrendada'),
                (2, 'Promesa de venta'),
                (3, 'Prestada'),
                (4, 'Tierra Indígena'),
                (5, 'Sin escritura'),
                (6, 'Colectivo/Cooperativa'),
              )
CHOICE_EDAD = (
                (1, 'Hombres > 31 años'),
                (2, 'Mujeres > 31 años'),
                (3, 'Ancianos > 64 años'),
                (4, 'Ancianas > 64 años'),
                (5, 'Mujer joven de 19 a 30 años'),
                (6, 'Hombre joven de 19 a 30 años'),
                (7, 'Mujer adolescente 13 a 18 años'),
                (8, 'Hombre adolescente 13 a 18 años'),
                (9, 'Niñas 5 a 12 años'),
                (10, 'Niños 5 a 12 años '),
                (11, 'Niñas 0 a 4 años '),
                (12, 'Niños 0 a 4 años'),
              )
CHOICE_ESCOLARIDAD = (
                (1, 'Hombres mayores 31 años'),
                (2, 'Mujeres mayores 31 años'),
                (3, 'Hombre joven de 19 a 30 años'),
                (4, 'Mujer joven de 19 a 30 años'),
                (5, 'Hombre adolescente 13 a 18 años'),
                (6, 'Mujer adolescente 13 a 18 años'),
                (7, 'Niños 5 a 12 años'),
                (8, 'Niñas 5 a 12 años '),
              )
# FIN DE CHOICES ESTATICOS


class Encuestadores(models.Model):
    nombre = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Encuestador'
        verbose_name_plural = 'Encuestadores'


class OrganizacionResp(models.Model):
    nombre = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Organización responsable'
        verbose_name_plural = 'Organizaciones responsables'


class Entrevistados(models.Model):
    nombre = models.CharField('Nombre Completo', max_length=250)
    cedula = models.CharField('No. Cédula', max_length=50)
    ocupacion = models.CharField('Ocupación', max_length=150)
    sexo = models.IntegerField(choices=CHOICE_SEXO)
    jefe = models.IntegerField(choices=CHOICE_JEFE, verbose_name='Jefe del hogar')
    edad = models.IntegerField()
    latitud = models.FloatField()
    longitud = models.FloatField()
    pais = models.ForeignKey(Pais)
    departamento = models.ForeignKey(Departamento)
    municipio = models.ForeignKey(Municipio)
    comunidad = models.ForeignKey(Comunidad)
    finca = models.CharField('Nombre de la finca', max_length=250)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Entrevistado'
        verbose_name_plural = 'Entrevistados'


class Encuesta(models.Model):
    entrevistado = models.ForeignKey(Entrevistados)
    dueno = models.IntegerField(choices=CHOICE_JEFE,
                    verbose_name='¿Son dueños de la propiedad/finca?')

    def __unicode__(self):
        return u'%s' % (self.entrevistado.nombre)


class DuenoSi(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    si = models.IntegerField(choices=CHOICE_DUENO_SI)

    def __unicode__(self):
        return u'%s' % (self.get_si_display())

    class Meta:
        verbose_name_plural = '6.1_En el caso SI, indique a nombre de quien está'


class DuenoNo(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    no = models.IntegerField(choices=CHOICE_DUENO_NO)

    def __unicode__(self):
        return u'%s' % (self.get_si_display())

    class Meta:
        verbose_name_plural = '6.2_En el caso que diga NO, especifique la situación'


class SexoMiembros(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    sexo = models.IntegerField(choices=CHOICE_SEXO,
                verbose_name='7_Sexo del jefe (a) del hogar')
    cantidad = models.IntegerField('8_Cantidad de personas que habitan en el hogar')

    def __unicode__(self):
        return u'%s' % (self.get_sexo_display())

    class Meta:
        verbose_name_plural = 'Sexo del jefe del hogar y cantidad de miembros'


class DetalleMiembros(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    edad = models.IntegerField(choices=CHOICE_EDAD)
    cantidad = models.IntegerField()

    def __unicode__(self):
        return u'%s' % (self.get_sexo_display())

    class Meta:
        verbose_name_plural = '9_Detalle la cantidad de miembros del hogar según edad y sexo'


class Escolaridad(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    sexo = models.IntegerField(choices=CHOICE_ESCOLARIDAD)
    no_leer = models.IntegerField('No lee,ni escribe')
    pri_incompleta = models.IntegerField('Primaria incompleta')
    pri_completa = models.IntegerField('Primaria completa')
    secu_incompleta = models.IntegerField('Secundaria incompleta')
    secu_completa = models.IntegerField('Secundaria completa')
    bachiller = models.IntegerField('Bachiller')
    uni_tecnico = models.IntegerField('Universitario o técnico')
    total = models.IntegerField('total')

    def __unicode__(self):
        return u'%s' % (self.get_sexo_display())

    class Meta:
        verbose_name_plural = '10_Nivel de escolaridad (número por categoría)'



















