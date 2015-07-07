# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lugar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccesoAgua',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name_plural': '14_Indique la forma que accede al agua para consumo humano',
            },
        ),
        migrations.CreateModel(
            name='AdquiereAgua',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='AguaConsumo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Agua para consumo',
                'verbose_name_plural': 'Agua para consumo',
            },
        ),
        migrations.CreateModel(
            name='AlimentosFueraFinca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.FloatField(verbose_name=b'Cantidad mensual')),
                ('precio', models.FloatField(verbose_name=b'Precio en C$')),
            ],
            options={
                'verbose_name_plural': '43_Indique los alimentos que compra fuera de la finca',
            },
        ),
        migrations.CreateModel(
            name='Animales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=4)),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='BeneficiosOrganizados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='CalidadAgua',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calidad', models.IntegerField(choices=[(1, b'De buena calidad'), (2, b'De regular calidad'), (3, b'Contaminada'), (4, b'No sabe')])),
            ],
            options={
                'verbose_name_plural': '16_Seg\xfan Usted, c\xf3mo es la calidad del agua que consume',
            },
        ),
        migrations.CreateModel(
            name='Cocinas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Tipo Cocina',
                'verbose_name_plural': 'Tipos de cocinas',
            },
        ),
        migrations.CreateModel(
            name='Contaminada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name_plural': '16.1_En caso de que est\xe9 contaminada, se\xf1ala posibles causas',
            },
        ),
        migrations.CreateModel(
            name='Cultivos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=4)),
                ('nombre', models.CharField(max_length=250)),
                ('unidad_medida', models.IntegerField(choices=[(1, b'Quintal'), (2, b'Libras'), (3, b'Docena'), (4, b'Cien'), (5, b'Cabeza')])),
            ],
        ),
        migrations.CreateModel(
            name='CultivosHuertos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=4)),
                ('nombre', models.CharField(max_length=250)),
                ('unidad_medida', models.IntegerField(choices=[(1, b'Quintal'), (2, b'Libras'), (3, b'Docena'), (4, b'Cien'), (5, b'Cabeza')])),
            ],
        ),
        migrations.CreateModel(
            name='CultivosHuertosFamiliares',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad_cosechada', models.FloatField()),
                ('consumo_familia', models.FloatField(verbose_name=b'Consumo de la familia')),
                ('consumo_animal', models.FloatField()),
                ('procesamiento', models.FloatField()),
                ('venta', models.FloatField()),
                ('precio', models.FloatField(verbose_name=b'Precio de venta en C$')),
                ('costo', models.FloatField(verbose_name=b'Costo por Mz en C$')),
                ('cultivo', models.ForeignKey(to='encuestas.CultivosHuertos')),
            ],
            options={
                'verbose_name_plural': '23_Cultivos de huertos familiares en la finca',
            },
        ),
        migrations.CreateModel(
            name='CultivosTradicionales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area_sembrada', models.FloatField(verbose_name=b'Area sembrada (Mz)')),
                ('area_cosechada', models.FloatField(verbose_name=b'Area cosechada (Mz)')),
                ('cantidad_cosechada', models.FloatField()),
                ('consumo_familia', models.FloatField(verbose_name=b'Consumo de la familia')),
                ('consumo_animal', models.FloatField()),
                ('procesamiento', models.FloatField()),
                ('venta', models.FloatField()),
                ('precio', models.FloatField(verbose_name=b'Precio de venta en C$')),
                ('costo', models.FloatField(verbose_name=b'Costo por Mz en C$')),
                ('periodo', models.IntegerField(choices=[(1, b'Primera'), (2, b'Postrera')])),
                ('cultivo', models.ForeignKey(to='encuestas.Cultivos')),
            ],
            options={
                'verbose_name_plural': '22_Cultivos tradicionales  producidos en la finca',
            },
        ),
        migrations.CreateModel(
            name='DetalleMiembros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('edad', models.IntegerField(choices=[(1, b'Hombres > 31 a\xc3\xb1os'), (2, b'Mujeres > 31 a\xc3\xb1os'), (3, b'Ancianos > 64 a\xc3\xb1os'), (4, b'Ancianas > 64 a\xc3\xb1os'), (5, b'Mujer joven de 19 a 30 a\xc3\xb1os'), (6, b'Hombre joven de 19 a 30 a\xc3\xb1os'), (7, b'Mujer adolescente 13 a 18 a\xc3\xb1os'), (8, b'Hombre adolescente 13 a 18 a\xc3\xb1os'), (9, b'Ni\xc3\xb1as 5 a 12 a\xc3\xb1os'), (10, b'Ni\xc3\xb1os 5 a 12 a\xc3\xb1os '), (11, b'Ni\xc3\xb1as 0 a 4 a\xc3\xb1os '), (12, b'Ni\xc3\xb1os 0 a 4 a\xc3\xb1os')])),
                ('cantidad', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': '9_Detalle la cantidad de miembros del hogar seg\xfan edad y sexo',
            },
        ),
        migrations.CreateModel(
            name='DisponibilidadAgua',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disponibilidad', models.IntegerField(choices=[(1, b'Todo los d\xc3\xadas y toda hora'), (2, b'Cada dos d\xc3\xadas y algunas horas'), (3, b'Algunos d\xc3\xadas y algunas horas'), (4, b'No confiable')])),
            ],
            options={
                'verbose_name_plural': '15_Mencione la disponibilidad del agua para consumo humano (en verano)',
            },
        ),
        migrations.CreateModel(
            name='DistribucionTierra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tierra', models.IntegerField(verbose_name=b'20.1_Distribuci\xc3\xb3n de la tierra en la finca', choices=[(1, b'Bosque'), (2, b'Tacotal'), (3, b'Cultivo anual'), (4, b'Plantaci\xc3\xb3n forestal'), (5, b'Potrero'), (6, b'Pasto en asocio con \xc3\xa1rboles'), (7, b'Frutales'), (8, b'Cultivos en asocio')])),
                ('manzanas', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='DuenoNo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('no', models.IntegerField(choices=[(1, b'Arrendada'), (2, b'Promesa de venta'), (3, b'Prestada'), (4, b'Tierra Ind\xc3\xadgena'), (5, b'Sin escritura'), (6, b'Colectivo/Cooperativa')])),
            ],
            options={
                'verbose_name_plural': '6.2_En el caso que diga NO, especifique la situaci\xf3n',
            },
        ),
        migrations.CreateModel(
            name='DuenoSi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('si', models.IntegerField(choices=[(1, b'A nombre del hombre'), (2, b'A nombre de la mujer'), (3, b'A nombre de los hijos'), (4, b'Mancomunado')])),
            ],
            options={
                'verbose_name_plural': '6.1_En el caso SI, indique a nombre de quien est\xe1',
            },
        ),
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('mapa_finca', sorl.thumbnail.fields.ImageField(upload_to=b'mapas_fincas')),
                ('dueno', models.IntegerField(verbose_name=b'\xc2\xbfSon due\xc3\xb1os de la propiedad/finca?', choices=[(1, b'Si'), (2, b'No')])),
                ('year', models.IntegerField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Encuestadores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Encuestador',
                'verbose_name_plural': 'Encuestadores',
            },
        ),
        migrations.CreateModel(
            name='Energia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Energia',
                'verbose_name_plural': 'Energias',
            },
        ),
        migrations.CreateModel(
            name='EnergiaSolarCocinar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': '12_Mencione el tipo de fuente de energ\xeda utiliza para cocinar',
            },
        ),
        migrations.CreateModel(
            name='Entrevistados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250, verbose_name=b'Nombre Completo')),
                ('cedula', models.CharField(max_length=50, verbose_name=b'No. C\xc3\xa9dula')),
                ('ocupacion', models.CharField(max_length=150, verbose_name=b'Ocupaci\xc3\xb3n')),
                ('sexo', models.IntegerField(choices=[(1, b'Mujer'), (2, b'Hombre')])),
                ('jefe', models.IntegerField(verbose_name=b'Jefe del hogar', choices=[(1, b'Si'), (2, b'No')])),
                ('edad', models.IntegerField()),
                ('latitud', models.FloatField(blank=True)),
                ('longitud', models.FloatField(blank=True)),
                ('finca', models.CharField(max_length=250, verbose_name=b'Nombre de la finca')),
                ('comunidad', models.ForeignKey(to='lugar.Comunidad')),
                ('departamento', models.ForeignKey(to='lugar.Departamento')),
                ('municipio', models.ForeignKey(to='lugar.Municipio')),
                ('pais', models.ForeignKey(to='lugar.Pais')),
            ],
            options={
                'verbose_name': 'Entrevistado',
                'verbose_name_plural': 'Entrevistados',
            },
        ),
        migrations.CreateModel(
            name='Escolaridad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sexo', models.IntegerField(choices=[(1, b'Hombres mayores 31 a\xc3\xb1os'), (2, b'Mujeres mayores 31 a\xc3\xb1os'), (3, b'Hombre joven de 19 a 30 a\xc3\xb1os'), (4, b'Mujer joven de 19 a 30 a\xc3\xb1os'), (5, b'Hombre adolescente 13 a 18 a\xc3\xb1os'), (6, b'Mujer adolescente 13 a 18 a\xc3\xb1os'), (7, b'Ni\xc3\xb1os 5 a 12 a\xc3\xb1os'), (8, b'Ni\xc3\xb1as 5 a 12 a\xc3\xb1os ')])),
                ('no_leer', models.IntegerField(verbose_name=b'No lee,ni escribe')),
                ('pri_incompleta', models.IntegerField(verbose_name=b'Primaria incompleta')),
                ('pri_completa', models.IntegerField(verbose_name=b'Primaria completa')),
                ('secu_incompleta', models.IntegerField(verbose_name=b'Secundaria incompleta')),
                ('secu_completa', models.IntegerField(verbose_name=b'Secundaria completa')),
                ('bachiller', models.IntegerField(verbose_name=b'Bachiller')),
                ('uni_tecnico', models.IntegerField(verbose_name=b'Universitario o t\xc3\xa9cnico')),
                ('total', models.IntegerField(verbose_name=b'total')),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': '10_Nivel de escolaridad (n\xfamero por categor\xeda)',
            },
        ),
        migrations.CreateModel(
            name='Evidencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cual', models.CharField(max_length=250, verbose_name=b'\xc2\xbfCu\xc3\xa1l?')),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': '16.2_Existe alguna evidencia',
            },
        ),
        migrations.CreateModel(
            name='FuenteEnergia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Fuente de Energia',
                'verbose_name_plural': 'Fuentes de Energias',
            },
        ),
        migrations.CreateModel(
            name='Fuentes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.FloatField(verbose_name=b'Cantidad mensual C$')),
                ('cantidad_veces', models.FloatField(verbose_name=b'Cantidad de veces en el a\xc3\xb1o')),
                ('hombres', models.IntegerField(verbose_name=b'Cantidad de miembros hombres')),
                ('mujeres', models.IntegerField(verbose_name=b'Cantidad de miembros mujeres')),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': '21_ingresos diferentes a la actividad agropecuaria',
            },
        ),
        migrations.CreateModel(
            name='Ganaderia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField(verbose_name=b'Cantidad de animales')),
                ('si_no', models.IntegerField(choices=[(1, b'Si'), (2, b'No')])),
                ('cantidad_vendida', models.IntegerField(verbose_name=b'Cantidad vendida este a\xc3\xb1o')),
                ('precio', models.FloatField(verbose_name=b'Precio de venta en C$')),
                ('animal', models.ForeignKey(to='encuestas.Animales')),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': '24_1 Inventario de ganaderia mayor y menor',
            },
        ),
        migrations.CreateModel(
            name='GastoHogar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.IntegerField(choices=[(1, b'Salud'), (2, b'Educaci\xc3\xb3n'), (3, b'Alquiler de vivienda'), (4, b'Ropa'), (5, b'Alimentaci\xc3\xb3n'), (6, b'Recreaci\xc3\xb3n/Diversi\xc3\xb3n')])),
                ('cantidad', models.FloatField(verbose_name=b'Cantidad mensual en C$')),
                ('cantidad_veces', models.FloatField(verbose_name=b'Cantidad de veces en el a\xc3\xb1o')),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': 'Gastos generales del hogar',
            },
        ),
        migrations.CreateModel(
            name='GastoProduccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.FloatField(verbose_name=b'Cantidad mensual en C$')),
                ('cantidad_veces', models.FloatField(verbose_name=b'Cantidad de veces en el a\xc3\xb1o')),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': 'Gastos generales para la producci\xf3n',
            },
        ),
        migrations.CreateModel(
            name='IntroducidosHuertos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('si_no', models.IntegerField(choices=[(1, b'Si'), (2, b'No')])),
                ('anio', models.IntegerField(verbose_name=b'A\xc3\xb1o')),
                ('cultivo', models.ForeignKey(to='encuestas.Cultivos')),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': 'Productos introducidos/promovidos huertos familiares',
            },
        ),
        migrations.CreateModel(
            name='IntroducidosTradicionales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('si_no', models.IntegerField(choices=[(1, b'Si'), (2, b'No')])),
                ('anio', models.IntegerField(verbose_name=b'A\xc3\xb1o')),
                ('cultivo', models.ForeignKey(to='encuestas.Cultivos')),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': 'Productos introducidos/promovidos tradicionales',
            },
        ),
        migrations.CreateModel(
            name='OrganizacionComunitaria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pertenece', models.IntegerField(verbose_name=b'19_\xc2\xbfPertenece a alguna organizaci\xc3\xb3n?', choices=[(1, b'Si'), (2, b'No')])),
            ],
        ),
        migrations.CreateModel(
            name='OrganizacionFinca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area_finca', models.FloatField(verbose_name=b'20_\xc2\xbfCu\xc3\xa1l es el \xc3\xa1rea total en manzana de la finca?')),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizacionResp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Organizaci\xf3n responsable',
                'verbose_name_plural': 'Organizaciones responsables',
            },
        ),
        migrations.CreateModel(
            name='OrgComunitarias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='OtrasSeguridad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tratamiento', models.IntegerField(verbose_name=b'42_1 Le da alg\xc3\xban tipo de tratamiento:', choices=[(1, b'Si'), (2, b'No')])),
                ('adquiere_agua', models.ForeignKey(verbose_name=b'42_En momentos de sequ\xc3\xada como adquiere el agua de consumo', to='encuestas.AdquiereAgua')),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': 'Pregunta 42',
            },
        ),
        migrations.CreateModel(
            name='PanelSolar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('panel', models.IntegerField(choices=[(1, b'Dom\xc3\xa9stico'), (2, b'Agr\xc3\xadcola'), (3, b'Negocio')])),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': '11.1_En el caso que tenga panel solar, cu\xe1l es el fin',
            },
        ),
        migrations.CreateModel(
            name='PercibeIngreso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('si_no', models.IntegerField(choices=[(1, b'Si'), (2, b'No')])),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
        ),
        migrations.CreateModel(
            name='Practicas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='PracticasAgroecologicas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('si_no', models.IntegerField(verbose_name=b'29_\xc2\xbfEn la finca aplican t\xc3\xa9cnicas de manejo agro ecologico u org\xc3\xa1nico', choices=[(1, b'Si'), (2, b'No')])),
                ('manejo', models.IntegerField(choices=[(1, b'Tala y quema'), (2, b'Trabaja en crudo'), (3, b'Arado'), (4, b'Uso de cobertura')])),
                ('traccion', models.IntegerField(choices=[(1, b'Animal'), (2, b'Humana'), (3, b'Tractor'), (4, b'Ninguna')])),
                ('fertilidad', models.IntegerField(choices=[(1, b'Si'), (2, b'No')])),
                ('control', models.IntegerField(choices=[(1, b'Si'), (2, b'No')])),
                ('cinco_principales', models.ManyToManyField(to='encuestas.Practicas', verbose_name=b'29.1_Mencione cinco principales')),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': 'Pr\xe1cticas agroecol\xf3gicas',
            },
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('algun_prestamo', models.IntegerField(choices=[(1, b'Si'), (2, b'No')])),
                ('monto', models.FloatField(verbose_name=b'28.1_\xc2\xbfCu\xc3\xa1l fue el monto en C$?')),
                ('pago', models.FloatField(verbose_name=b'28.2_\xc2\xbfPago mensual en C$?')),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': '28_En el ultimo a\xf1o ha recibido alg\xfan tipo de prestamo/cr\xe9dito',
            },
        ),
        migrations.CreateModel(
            name='Procesamiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField(verbose_name=b'Cantidad')),
                ('cantidad_vendida', models.IntegerField(verbose_name=b'Cantidad vendida este a\xc3\xb1o')),
                ('precio', models.FloatField(verbose_name=b'Precio de venta en C$')),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': '24_2 Procesamiento de la producci\xf3n',
            },
        ),
        migrations.CreateModel(
            name='ProductoProcesado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
                ('unidad_medida', models.IntegerField(choices=[(1, b'Quintal'), (2, b'Libras'), (3, b'Docena'), (4, b'Cien'), (5, b'Cabeza')])),
            ],
        ),
        migrations.CreateModel(
            name='ProductosFueraFinca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
                ('unidad_medida', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='RecibePrestamo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='RespuestaNo41',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fenomeno', multiselectfield.db.fields.MultiSelectField(max_length=200, verbose_name=((1, b'Falta de cr\xc3\xa9dito'), (2, b'Alto inter\xc3\xa9s')))),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': '41.1_Si responde NO, marque con una X las principales razones',
            },
        ),
        migrations.CreateModel(
            name='SeguridadAlimentaria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('misma_finca', models.IntegerField(verbose_name=b'35.1_\xc2\xbfQu\xc3\xa9 porcentaje alimentos que consumen en su hogar provienen de la misma finca?', choices=[(1, b'10%'), (2, b'20%'), (3, b'30%'), (4, b'40%'), (5, b'50%'), (6, b'60%'), (7, b'70%'), (8, b'80%'), (9, b'90%'), (10, b'100%')])),
                ('fuera_finca', models.IntegerField(verbose_name=b'35.2_\xc2\xbfQu\xc3\xa9 porcentaje alimentos que consumen en su hogar provienen fuera de la finca?', choices=[(1, b'10%'), (2, b'20%'), (3, b'30%'), (4, b'40%'), (5, b'50%'), (6, b'60%'), (7, b'70%'), (8, b'80%'), (9, b'90%'), (10, b'100%')])),
                ('economico', models.IntegerField(verbose_name=b'36_\xc2\xbfDisponen suficiente recursos econ\xc3\xb3micos para manejo de finca?', choices=[(1, b'Si'), (2, b'No')])),
                ('secado', models.IntegerField(verbose_name=b'37_\xc2\xbfDispone de tecnolog\xc3\xada para el secado y almacenamiento de cosecha?', choices=[(1, b'Si'), (2, b'No')])),
                ('plan_cosecha', models.IntegerField(verbose_name=b'38_\xc2\xbfCuentan con un plan de cosecha?', choices=[(1, b'Si'), (2, b'No')])),
                ('ayuda', models.IntegerField(verbose_name=b'39_\xc2\xbfCuentan con ayuda de alimentos en momentos de escasez?', choices=[(1, b'Si'), (2, b'No')])),
                ('suficiente_alimento', models.IntegerField(verbose_name=b'40_\xc2\xbfLe ha preocupado que en su hogar no hubiera suficiente alimentos?', choices=[(1, b'Si'), (2, b'No')])),
                ('consumo_diario', models.IntegerField(verbose_name=b'41_\xc2\xbfConsidera que su familia cuenta con la cantidad necesaria de alimentos que necesitan para el consumo diario del hogar?', choices=[(1, b'Si'), (2, b'No')])),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': 'VI. Seguridad alimentaria',
            },
        ),
        migrations.CreateModel(
            name='SexoMiembros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sexo', models.IntegerField(verbose_name=b'7_Sexo del jefe (a) del hogar', choices=[(1, b'Mujer'), (2, b'Hombre')])),
                ('cantidad', models.IntegerField(verbose_name=b'8_Cantidad de personas que habitan en el hogar')),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': 'Sexo del jefe del hogar y cantidad de miembros',
            },
        ),
        migrations.CreateModel(
            name='TipoCocinas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cocina', models.ManyToManyField(to='encuestas.Cocinas')),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': '13_Mencione el tipo de cocina que utiliza para cocinar',
            },
        ),
        migrations.CreateModel(
            name='TipoContamindaAgua',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Tipo agua contaminada',
                'verbose_name_plural': 'Tipo agua contaminada',
            },
        ),
        migrations.CreateModel(
            name='TipoEnergia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
                ('tipo', models.ManyToManyField(to='encuestas.Energia')),
            ],
            options={
                'verbose_name_plural': '11_\xbfQu\xe9 tipo de energ\xeda utiliza para alumbrar la vivienda?',
            },
        ),
        migrations.CreateModel(
            name='TipoFuenteIngreso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.IntegerField(choices=[(1, b'Asalariado'), (2, b'Jornalero'), (3, b'Alquiler'), (4, b'Negocio propio'), (5, b'Remesas'), (6, b'Otros')])),
                ('nombre', models.CharField(max_length=250, verbose_name=b'especifique tipo')),
            ],
        ),
        migrations.CreateModel(
            name='TipoGasto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='TipoMercado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=4)),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='TipoSecado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='TrataAgua',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='TratamientoAgua',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tratamiento', models.IntegerField(choices=[(1, b'Se hierve'), (2, b'Se clora'), (3, b'Se usa filtro'), (4, b'Se deja reposar'), (5, b'Ninguno')])),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': '17_Realiza alg\xfan tratamiento al agua de consumo',
            },
        ),
        migrations.CreateModel(
            name='UsoPrestamo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='UsosAgua',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uso', models.IntegerField(choices=[(1, b'Uso dom\xc3\xa9stico'), (2, b'Uso agr\xc3\xadcola'), (3, b'Uso tur\xc3\xadstico'), (4, b'Crianza de peces'), (5, b'Para ganado')])),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': '18_Indique qu\xe9 otros usos le dan al agua en la finca',
            },
        ),
        migrations.AddField(
            model_name='seguridadalimentaria',
            name='tipo_secado',
            field=models.ForeignKey(verbose_name=b'Si es si cu\xc3\xa1l?', to='encuestas.TipoSecado'),
        ),
        migrations.AddField(
            model_name='procesamiento',
            name='mercado',
            field=models.ForeignKey(to='encuestas.TipoMercado'),
        ),
        migrations.AddField(
            model_name='procesamiento',
            name='producto',
            field=models.ForeignKey(to='encuestas.ProductoProcesado'),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='recibe',
            field=models.ManyToManyField(to='encuestas.RecibePrestamo', verbose_name=b'28.3_\xc2\xbfDe quien recibe el prestamo/cr\xc3\xa9dito'),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='uso',
            field=models.ManyToManyField(to='encuestas.UsoPrestamo', verbose_name=b'28.4_\xc2\xbfCu\xc3\xa1l fue el uso del prestamo/cr\xc3\xa9dito'),
        ),
        migrations.AddField(
            model_name='otrasseguridad',
            name='tipo_tratamiento',
            field=models.ForeignKey(to='encuestas.TrataAgua'),
        ),
        migrations.AddField(
            model_name='organizacioncomunitaria',
            name='caso_si',
            field=models.ManyToManyField(to='encuestas.OrgComunitarias', verbose_name=b'19_1 qu\xc3\xa9 organizaci\xc3\xb3n comunitaria pertenece?'),
        ),
        migrations.AddField(
            model_name='organizacioncomunitaria',
            name='cuales_beneficios',
            field=models.ManyToManyField(to='encuestas.BeneficiosOrganizados', verbose_name=b'19_2 \xc2\xbfCuales son los beneficios de estar organizado?'),
        ),
        migrations.AddField(
            model_name='organizacioncomunitaria',
            name='encuesta',
            field=models.ForeignKey(to='encuestas.Encuesta'),
        ),
        migrations.AddField(
            model_name='gastoproduccion',
            name='tipo',
            field=models.ForeignKey(to='encuestas.TipoGasto'),
        ),
        migrations.AddField(
            model_name='ganaderia',
            name='mercado',
            field=models.ForeignKey(to='encuestas.TipoMercado'),
        ),
        migrations.AddField(
            model_name='fuentes',
            name='fuente_ingreso',
            field=models.ForeignKey(to='encuestas.TipoFuenteIngreso'),
        ),
        migrations.AddField(
            model_name='energiasolarcocinar',
            name='fuente',
            field=models.ManyToManyField(to='encuestas.FuenteEnergia'),
        ),
        migrations.AddField(
            model_name='encuesta',
            name='entrevistado',
            field=models.ForeignKey(to='encuestas.Entrevistados'),
        ),
        migrations.AddField(
            model_name='duenosi',
            name='encuesta',
            field=models.ForeignKey(to='encuestas.Encuesta'),
        ),
        migrations.AddField(
            model_name='duenono',
            name='encuesta',
            field=models.ForeignKey(to='encuestas.Encuesta'),
        ),
        migrations.AddField(
            model_name='distribuciontierra',
            name='encuesta',
            field=models.ForeignKey(to='encuestas.Encuesta'),
        ),
        migrations.AddField(
            model_name='disponibilidadagua',
            name='encuesta',
            field=models.ForeignKey(to='encuestas.Encuesta'),
        ),
        migrations.AddField(
            model_name='detallemiembros',
            name='encuesta',
            field=models.ForeignKey(to='encuestas.Encuesta'),
        ),
        migrations.AddField(
            model_name='cultivostradicionales',
            name='encuesta',
            field=models.ForeignKey(to='encuestas.Encuesta'),
        ),
        migrations.AddField(
            model_name='cultivostradicionales',
            name='mercado',
            field=models.ForeignKey(to='encuestas.TipoMercado'),
        ),
        migrations.AddField(
            model_name='cultivoshuertosfamiliares',
            name='encuesta',
            field=models.ForeignKey(to='encuestas.Encuesta'),
        ),
        migrations.AddField(
            model_name='cultivoshuertosfamiliares',
            name='mercado',
            field=models.ForeignKey(to='encuestas.TipoMercado'),
        ),
        migrations.AddField(
            model_name='contaminada',
            name='contaminada',
            field=models.ForeignKey(to='encuestas.TipoContamindaAgua'),
        ),
        migrations.AddField(
            model_name='contaminada',
            name='encuesta',
            field=models.ForeignKey(to='encuestas.Encuesta'),
        ),
        migrations.AddField(
            model_name='calidadagua',
            name='encuesta',
            field=models.ForeignKey(to='encuestas.Encuesta'),
        ),
        migrations.AddField(
            model_name='alimentosfuerafinca',
            name='encuesta',
            field=models.ForeignKey(to='encuestas.Encuesta'),
        ),
        migrations.AddField(
            model_name='alimentosfuerafinca',
            name='producto',
            field=models.ForeignKey(to='encuestas.ProductosFueraFinca'),
        ),
        migrations.AddField(
            model_name='accesoagua',
            name='agua',
            field=models.ManyToManyField(to='encuestas.AguaConsumo'),
        ),
        migrations.AddField(
            model_name='accesoagua',
            name='encuesta',
            field=models.ForeignKey(to='encuestas.Encuesta'),
        ),
    ]
