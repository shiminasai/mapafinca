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
    latitud = models.FloatField(blank=True)
    longitud = models.FloatField(blank=True)
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
    fecha = models.DateField()
    dueno = models.IntegerField(choices=CHOICE_JEFE,
                    verbose_name='¿Son dueños de la propiedad/finca?')

    year = models.IntegerField(editable=False)

    def save(self):
        self.year = self.fecha.year
        super(Encuesta, self).save()

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


class Energia(models.Model):
    nombre = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Energia'
        verbose_name_plural = 'Energias'

class TipoEnergia(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    tipo = models.ManyToManyField(Energia)

    class Meta:
        verbose_name_plural = '11_¿Qué tipo de energía utiliza para alumbrar la vivienda?'

CHOICE_PANEL_SOLAR = (
                (1, 'Doméstico'),
                (2, 'Agrícola'),
                (3, 'Negocio'),
              )

class PanelSolar(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    panel = models.IntegerField(choices=CHOICE_PANEL_SOLAR)

    class Meta:
        verbose_name_plural = '11.1_En el caso que tenga panel solar, cuál es el fin'


class FuenteEnergia(models.Model):
    nombre = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Fuente de Energia'
        verbose_name_plural = 'Fuentes de Energias'


class PanelSolar(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    fuente = models.ManyToManyField(FuenteEnergia)

    class Meta:
        verbose_name_plural = '12_Mencione el tipo de fuente de energía utiliza para cocinar'


class Cocinas(models.Model):
    nombre = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tipo Cocina'
        verbose_name_plural = 'Tipos de cocinas'


class TipoCocinas(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    cocina = models.ManyToManyField(Cocinas)

    class Meta:
        verbose_name_plural = '13_Mencione el tipo de cocina que utiliza para cocinar'

class AguaConsumo(models.Model):
    nombre = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Agua para consumo'
        verbose_name_plural = 'Agua para consumo'


class AccesoAgua(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    agua = models.ManyToManyField(AguaConsumo)

    class Meta:
        verbose_name_plural = '14_Indique la forma que accede al agua para consumo humano'


CHOICE_DISPONIBILIDAD = (
                (1, 'Todo los días y toda hora'),
                (2, 'Cada dos días y algunas horas'),
                (3, 'Algunos días y algunas horas'),
                (4, 'No confiable')
              )


class AccesoAgua(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    disponibilidad = models.IntegerField(choices=CHOICE_DISPONIBILIDAD)

    class Meta:
        verbose_name_plural = '15_Mencione la disponibilidad del agua para consumo humano (en verano)'


CHOICE_CALIDAD_AGUA = (
                (1, 'De buena calidad'),
                (2, 'De regular calidad'),
                (3, 'Contaminada'),
                (4, 'No sabe')
              )


class AccesoAgua(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    calidad = models.IntegerField(choices=CHOICE_CALIDAD_AGUA)

    class Meta:
        verbose_name_plural = '16_Según Usted, cómo es la calidad del agua que consume'


class TipoContamindaAgua(models.Model):
    nombre = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tipo agua contaminada'
        verbose_name_plural = 'Tipo agua contaminada'

class Contaminada(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    contaminada = models.ForeignKey(TipoContamindaAgua)

    class Meta:
        verbose_name_plural = '16.1_En caso de que esté contaminada, señala posibles causas'

class Evidencia(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    cual = models.CharField('¿Cuál?', max_length=250)

    class Meta:
        verbose_name_plural = '16.2_Existe alguna evidencia'


CHOICE_TRATAMIENTO = (
                (1, 'Se hierve'),
                (2, 'Se clora'),
                (3, 'Se usa filtro'),
                (4, 'Se deja reposar'),
                (5, 'Ninguno')
              )

CHOICE_OTRO_USO = (
                (1, 'Uso doméstico'),
                (2, 'Uso agrícola'),
                (3, 'Uso turístico'),
                (4, 'Crianza de peces'),
                (5, 'Para ganado')
              )

class TratamientoAgua(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    tratamiento = models.IntegerField(choices=CHOICE_TRATAMIENTO)

    class Meta:
        verbose_name_plural = '17_Realiza algún tratamiento al agua de consumo'

class UsosAgua(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    uso = models.IntegerField(choices=CHOICE_OTRO_USO)

    class Meta:
        verbose_name_plural = '18_Indique qué otros usos le dan al agua en la finca'