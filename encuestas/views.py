# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.views.generic import TemplateView
from .forms import ConsultarForm
from .models import *
import json as simplejson
from django.db.models import Sum, Avg
from clima.models import *
from collections import OrderedDict
# Create your views here.


def _queryset_filtrado(request):
    params = {}
    if request.session['sexo']:
        params['entrevistado__sexo'] = request.session['sexo']

    if request.session['organizacion']:
        params['org_responsable'] = request.session['organizacion']

    return Encuesta.objects.filter(**params)


def IndexView(request,template="index.html"):
    if request.method == 'POST':
        mensaje = None
        form = ConsultarForm(request.POST)
        if form.is_valid():
            request.session['sexo'] = form.cleaned_data['sexo']
            request.session['organizacion'] = form.cleaned_data['organizacion']
            mensaje = "Todas las variables estan correctamente :)"
            request.session['activo'] = True
            centinela = 1

            return redirect('/mapa/')

        else:
            centinela = 0

    else:
        form = ConsultarForm()
        mensaje = "Existen alguno errores"
        centinela = 0
        try:
            del request.session['sexo']
            del request.session['organizacion']
        except:
            pass
        paises = {}
        for pais in Pais.objects.all():
            paises[pais] = {}
            for mun in Municipio.objects.all():
                m = Encuesta.objects.filter(entrevistado__municipio=mun, entrevistado__pais=pais).count()
                if m > 0:
                    paises[pais][mun.departamento.nombre] = (m,mun.departamento.id)

    return render(request, template, locals())


def obtener_mapa_dashboard(request):
    if request.is_ajax():
        lista = []
        for objeto in Encuesta.objects.all().distinct('entrevistado_id'):
            dicc = dict(nombre=objeto.entrevistado.nombre, id=objeto.id,
                        lon=float(objeto.entrevistado.municipio.longitud),
                        lat=float(objeto.entrevistado.municipio.latitud)
                        )
            lista.append(dicc)

        serializado = simplejson.dumps(lista)
        return HttpResponse(serializado, content_type='application/json')


class GalleryView(TemplateView):
    template_name = "galeria.html"

    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        context['object_list'] = Encuesta.objects.all()
        return context


class DetailIndicadorView(TemplateView):
    template_name = "detalle_indicador.html"


class FirstMapaView(TemplateView):
    template_name = "primer_mapa.html"

    def get_context_data(self, **kwargs):
        context = super(FirstMapaView, self).get_context_data(**kwargs)
        context['nicaragua'] = Encuesta.objects.filter(entrevistado__pais_id=1).count()
        context['elsalvado'] = 0  #Encuesta.objects.filter(entrevistado__pais_id=2).count()
        context['honduras'] = 0  #Encuesta.objects.filter(entrevistado__pais_id=3).count()
        context['guatemala'] = 0  #Encuesta.objects.filter(entrevistado__pais_id=4).count()
        return context


class MapaView(TemplateView):
    template_name = "mapa.html"

    def get_context_data(self, **kwargs):
        context = super(MapaView, self).get_context_data(**kwargs)
        context['nicaragua'] = Encuesta.objects.filter(entrevistado__pais_id=1).count()
        context['elsalvado'] = 0#Encuesta.objects.filter(entrevistado__pais_id=2).count()
        context['honduras'] = 0#Encuesta.objects.filter(entrevistado__pais_id=3).count()
        context['guatemala'] = 0#Encuesta.objects.filter(entrevistado__pais_id=4).count()
        return context

def principal_dashboard(request, template='dashboard.html', departamento_id=None):
    #a = _queryset_filtrado(request)
    ahora = Encuesta.objects.filter(entrevistado__departamento=departamento_id).distinct('entrevistado__id')
    depart = Departamento.objects.get(id=departamento_id)
    request.session['departamento'] = depart
    geolat = []
    geolong = []
    for obj in depart.municipio_set.all():
        geolat.append(obj.latitud)
        geolong.append(obj.longitud)

    latitud = geolat[-2]
    longitud = geolong[-2]

    # grafico de patron de gastos
    gasto_finca = Encuesta.objects.filter(entrevistado__departamento=departamento_id,gastohogar__tipo=5).aggregate(t=Sum('gastohogar__total'))['t']
    gasto_fuera_finca = Encuesta.objects.filter(entrevistado__departamento=departamento_id).aggregate(t=Sum('gastoproduccion__total'))['t']

    # grafico de ingresos
    tradicional = Encuesta.objects.filter(entrevistado__departamento=departamento_id).aggregate(t=Sum('cultivostradicionales__total'))['t']

    huertos = Encuesta.objects.filter(entrevistado__departamento=departamento_id).aggregate(t=Sum('cultivoshuertosfamiliares__total'))['t']

    fuente = Encuesta.objects.filter(entrevistado__departamento=departamento_id).aggregate(t=Sum('fuentes__total'))['t']

    ganado = Encuesta.objects.filter(entrevistado__departamento=departamento_id).aggregate(t=Sum('ganaderia__total'))['t']

    procesamiento = Encuesta.objects.filter(entrevistado__departamento=departamento_id).aggregate(t=Sum('procesamiento__total'))['t']

    #grafico de kcalorias aun esta en proceso

    #grafico sobre gastos alimentarios
    gastos_alimentarios = {}
    for obj in ProductosFueraFinca.objects.all():
        cada_uno = Encuesta.objects.filter(entrevistado__departamento=departamento_id, alimentosfuerafinca__producto=obj).aggregate(t=Avg('alimentosfuerafinca__total'))['t']
        if cada_uno == None:
            cada_uno = 0
        gastos_alimentarios[obj] = cada_uno

    #grafico sobre clima
    lista_precipitacion = []
    lista_temperatura = []
    for mes in CHOICES_MESES:
        precipitacion = Precipitacion.objects.filter(departamento=departamento_id,mes=mes[0]).aggregate(p=Avg('precipitacion'))['p']
        temperatura = Temperatura.objects.filter(departamento=departamento_id,mes=mes[0]).aggregate(p=Avg('temperatura'))['p']
        if precipitacion == None:
            precipitacion = 0
        lista_precipitacion.append(precipitacion)
        if temperatura == None:
            temperatura = 0
        lista_temperatura.append(temperatura)

    return render(request,template,locals())

def detalle_finca(request, template='detalle_finca.html', entrevistado_id=None):
    detalle = Encuesta.objects.filter(entrevistado_id=entrevistado_id).order_by('year')

    #años que tiene ese productor
    years = []
    for en in Encuesta.objects.filter(entrevistado_id=entrevistado_id).order_by('year').values_list('year', flat=True):
        years.append((en,en))
    list(set(years))

    #para el mapa
    latitud = 0
    longitud = 0
    for obj in detalle:
        if obj.entrevistado.latitud:
            latitud = obj.entrevistado.latitud
        else:
            latitud = obj.entrevistado.municipio.latitud
        if obj.entrevistado.longitud:
            longitud = obj.entrevistado.longitud
        else:
            longitud = obj.entrevistado.municipio.longitud
    #fin del mapa
    #los años del detalle del productor
    gran_dicc = {}
    for year in years:
        tabla_educacion = []
        grafo = []
        suma = 0
        for e in CHOICE_ESCOLARIDAD:
            objeto = detalle.filter(year=year[0],escolaridad__sexo = e[0]).aggregate(num_total = Sum('escolaridad__total'),
                    no_leer = Sum('escolaridad__no_leer'),
                    p_incompleta = Sum('escolaridad__pri_incompleta'),
                    p_completa = Sum('escolaridad__pri_completa'),
                    s_incompleta = Sum('escolaridad__secu_incompleta'),
                    bachiller = Sum('escolaridad__bachiller'),
                    universitario = Sum('escolaridad__uni_tecnico'))
            try:
                suma = int(objeto['p_completa'] or 0) + int(objeto['s_incompleta'] or 0) + int(objeto['bachiller'] or 0) + int(objeto['universitario'] or 0)
            except:
                pass
            variable = round(saca_porcentajes(suma,objeto['num_total']))
            grafo.append([e[1],variable])

        #calculo ingreso vs gasto
        gasto_total = detalle.filter(year=year[0]).aggregate(t=Sum('totalingreso__total_gasto'))['t']
        gasto_total_fuera = detalle.filter(year=year[0]).aggregate(t=Sum('totalingreso__total_gasto_fuera_finca'))['t']

        ingreso_total = detalle.filter(year=year[0]).aggregate(t=Sum('totalingreso__total'))['t']
        total_gastos = gasto_total + gasto_total_fuera

        gran_dicc[year[1]] = (grafo, ingreso_total, total_gastos)

    return render(request, template, locals())


def indicadores(request, template='indicadores.html'):
    #a = _queryset_filtrado(request)
    #indicadores = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento']).distinct('entrevistado__id')
    total_entrevistados = Entrevistados.objects.count()
    total_hombres = Entrevistados.objects.filter(sexo=2).count()
    total_mujeres = Entrevistados.objects.filter(sexo=1).count()

    porcentaje_hombres = total_hombres / total_entrevistados * 100
    porcentaje_mujeres = total_mujeres / total_entrevistados * 100

    organizaciones = OrganizacionResp.objects.count()
    familias = Entrevistados.objects.count()

    #años que tiene ese productor
    years = []
    for en in Encuesta.objects.order_by('year').values_list('year', flat=True):
        years.append((en,en))
    list(set(years))

    #-------- Ingresos por años ----------
    model_dict = {
    'Procesamiento': Procesamiento,
    'Ganaderia': Ganaderia,
    'Cultivos huertos familiares': CultivosHuertosFamiliares,
    'Cultivos tradicionales': CultivosTradicionales,
    'Fuentes': Fuentes,
    'Cultivos frutas finca': CultivosFrutasFinca,

    }

    dicc1 = OrderedDict()
    for name,value in model_dict.items():
        dicc1[name] = OrderedDict()
        for year in years:
            valor = value.objects.filter(encuesta__year=year[0]).aggregate(t=Sum('total'))['t']
            dicc1[name][year[1]] = valor

    #------------ Gasto del hogar ------
    dicc2 = OrderedDict()
    for obj in CHOICE_TIPO_GASTOS:
        dicc2[obj[1]] = OrderedDict()
        for year in years:
            valor = GastoHogar.objects.filter(encuesta__year=year[0], tipo=obj[0]).aggregate(t=Sum('total'))['t']
            dicc2[obj[1]][year[1]] = valor

    #Ingresos vs gastos por años
    ingreso_dicc = OrderedDict()
    for year in years:
        ingreso_total = Encuesta.objects.filter(year=year[0]).aggregate(t=Sum('totalingreso__total'))['t']
        total_poll = Encuesta.objects.filter(year=year[0]).count()
        try:
            porcentaje = saca_porcentajes(ingreso_total,total_poll,False)
        except:
            porcentaje = 0
        ingreso_dicc[year[1]] = porcentaje

    return render(request, template, locals())

#FUNCIONES PARA LAS DEMAS SALIDAS DEL SISTEMA

def sexo_duenos(request, template="indicadores/sexo_duenos.html"):
    si_dueno = Encuesta.objects.filter(dueno=1).count()
    no_dueno = Encuesta.objects.filter(dueno=2).count()

    a_nombre = {}
    for obj in CHOICE_DUENO_SI:
        conteos = Encuesta.objects.filter(duenosi__si=obj[0]).count()
        a_nombre[obj[1]] = conteos

    situacion = {}
    for obj in CHOICE_DUENO_NO:
        conteos = Encuesta.objects.filter(duenono__no=obj[0]).count()
        situacion[obj[1]] = conteos

    sexo_jefe_hogar = {}
    for obj in CHOICE_SEXO:
        conteos = Encuesta.objects.filter(sexomiembros__sexo=obj[0]).count()
        sexo_jefe_hogar[obj[1]] = conteos


    return render(request, template, locals())

def escolaridad(request, template="indicadores/escolaridad.html"):
    #filtro = _queryset_filtrado(request)

    tabla_educacion = []
    grafo = []
    suma = 0
    for e in CHOICE_ESCOLARIDAD:
        objeto = Encuesta.objects.filter(escolaridad__sexo = e[0]).aggregate(num_total = Sum('escolaridad__total'),
                no_leer = Sum('escolaridad__no_leer'),
                p_incompleta = Sum('escolaridad__pri_incompleta'),
                p_completa = Sum('escolaridad__pri_completa'),
                s_incompleta = Sum('escolaridad__secu_incompleta'),
                bachiller = Sum('escolaridad__bachiller'),
                universitario = Sum('escolaridad__uni_tecnico'),

                )
        try:
            suma = int(objeto['p_completa'] or 0) + int(objeto['s_incompleta'] or 0) + int(objeto['bachiller'] or 0) + int(objeto['universitario'] or 0)
        except:
            pass
        variable = round(saca_porcentajes(suma,objeto['num_total']))
        grafo.append([e[1],variable])
        fila = [e[1], objeto['num_total'],
                saca_porcentajes(objeto['no_leer'], objeto['num_total'], False),
                saca_porcentajes(objeto['p_incompleta'], objeto['num_total'], False),
                saca_porcentajes(objeto['p_completa'], objeto['num_total'], False),
                saca_porcentajes(objeto['s_incompleta'], objeto['num_total'], False),
                saca_porcentajes(objeto['bachiller'], objeto['num_total'], False),
                saca_porcentajes(objeto['universitario'], objeto['num_total'], False),
                ]
        tabla_educacion.append(fila)

    return render(request, template, locals())

def energia(request, template="indicadores/energia.html"):

    grafo_tipo_energia = {}
    for obj in Energia.objects.all():
        valor = Encuesta.objects.filter(tipoenergia__tipo=obj).count()
        grafo_tipo_energia[obj] =  valor

    grafo_panel_solar = {}
    for obj in CHOICE_PANEL_SOLAR:
        valor = Encuesta.objects.filter(panelsolar__panel=obj[0]).count()
        grafo_panel_solar[obj[1]] =  valor

    grafo_fuente_energia = {}
    for obj in FuenteEnergia.objects.all():
        valor = Encuesta.objects.filter(energiasolarcocinar__fuente=obj).count()
        grafo_fuente_energia[obj] =  valor

    grafo_tipo_cocina = {}
    for obj in Cocinas.objects.all():
        valor = Encuesta.objects.filter(tipococinas__cocina=obj).count()
        grafo_tipo_cocina[obj] =  valor


    return render(request, template, locals())

def agua(request, template="indicadores/agua.html"):

    grafo_agua_consumo = {}
    for obj in AguaConsumo.objects.all():
        valor = Encuesta.objects.filter(accesoagua__agua=obj).count()
        grafo_agua_consumo[obj] =  valor

    grafo_agua_disponibilidad = {}
    for obj in CHOICE_DISPONIBILIDAD:
        valor = Encuesta.objects.filter(disponibilidadagua__disponibilidad=obj[0]).count()
        grafo_agua_disponibilidad[obj[1]] =  valor

    grafo_agua_calidad = {}
    for obj in CHOICE_CALIDAD_AGUA:
        valor = Encuesta.objects.filter(calidadagua__calidad=obj[0]).count()
        grafo_agua_calidad[obj[1]] =  valor

    grafo_agua_contaminada = {}
    for obj in TipoContamindaAgua.objects.all():
        valor = Encuesta.objects.filter(contaminada__contaminada=obj).count()
        grafo_agua_contaminada[obj] =  valor

    grafo_agua_tratamiento = {}
    for obj in CHOICE_TRATAMIENTO:
        valor = Encuesta.objects.filter(tratamientoagua__tratamiento=obj[0]).count()
        grafo_agua_tratamiento[obj[1]] =  valor

    grafo_agua_usos = {}
    for obj in CHOICE_OTRO_USO:
        valor = Encuesta.objects.filter(usosagua__uso=obj[0]).count()
        grafo_agua_usos[obj[1]] =  valor


    return render(request, template, locals())

def organizaciones(request, template="indicadores/organizaciones.html"):

    grafo_pertenece = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(organizacioncomunitaria__pertenece=obj[0]).count()
        grafo_pertenece[obj[1]] =  valor

    grafo_org_comunitarias = {}
    for obj in OrgComunitarias.objects.all():
        valor = Encuesta.objects.filter(organizacioncomunitaria__caso_si=obj).count()
        grafo_org_comunitarias[obj] =  valor

    grafo_beneficios = {}
    for obj in BeneficiosOrganizados.objects.all():
        valor = Encuesta.objects.filter(organizacioncomunitaria__cuales_beneficios=obj).count()
        grafo_beneficios[obj] =  valor

    return render(request, template, locals())

def tierra(request, template="indicadores/tierra.html"):

    #promedio de manzanas por todas las personas
    promedio_mz = Encuesta.objects.aggregate(p=Avg('organizacionfinca__area_finca'))['p']

    grafo_distribucion_tierra = {}
    for obj in CHOICE_TIERRA:
        valor = Encuesta.objects.filter(distribuciontierra__tierra=obj[0]).count()
        grafo_distribucion_tierra[obj[1]] =  valor

    return render(request, template, locals())

def prestamos(request, template="indicadores/prestamo.html"):

    grafo_prestamo_sino = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(prestamo__algun_prestamo=obj[0]).count()
        grafo_prestamo_sino[obj[1]] =  valor

    grafo_recibe_prestamo = {}
    for obj in RecibePrestamo.objects.all():
        valor = Encuesta.objects.filter(prestamo__recibe=obj).count()
        grafo_recibe_prestamo[obj] =  valor

    grafo_uso_prestamo = {}
    for obj in UsoPrestamo.objects.all():
        valor = Encuesta.objects.filter(prestamo__uso=obj).count()
        grafo_uso_prestamo[obj] =  valor

    return render(request, template, locals())

def practicas(request, template="indicadores/practicas.html"):

    grafo_practicas_sino = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(practicasagroecologicas__si_no=obj[0]).count()
        grafo_practicas_sino[obj[1]] =  valor

    grafo_manejo = {}
    for obj in CHOICE_MANEJO:
        valor = Encuesta.objects.filter(practicasagroecologicas__manejo=obj[0]).count()
        grafo_manejo[obj[1]] =  valor

    grafo_traccion = {}
    for obj in CHOICE_TRACCION:
        valor = Encuesta.objects.filter(practicasagroecologicas__traccion=obj[0]).count()
        grafo_traccion[obj[1]] =  valor

    grafo_fertilidad = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(practicasagroecologicas__fertilidad=obj[0]).count()
        grafo_fertilidad[obj[1]] =  valor

    grafo_control = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(practicasagroecologicas__control=obj[0]).count()
        grafo_control[obj[1]] =  valor

    return render(request, template, locals())

def seguridad(request, template="indicadores/seguridad.html"):

    grafo_economico = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(seguridadalimentaria__economico=obj[0]).count()
        grafo_economico[obj[1]] =  valor

    grafo_secado = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(seguridadalimentaria__secado=obj[0]).count()
        grafo_secado[obj[1]] =  valor

    grafo_tipo_secado = {}
    for obj in TipoSecado.objects.all():
        valor = Encuesta.objects.filter(seguridadalimentaria__tipo_secado=obj).count()
        grafo_tipo_secado[obj] =  valor

    grafo_plan_cosecha = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(seguridadalimentaria__plan_cosecha=obj[0]).count()
        grafo_plan_cosecha[obj[1]] =  valor

    grafo_ayuda = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(seguridadalimentaria__ayuda=obj[0]).count()
        grafo_ayuda[obj[1]] =  valor

    grafo_suficiente_alimento = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(seguridadalimentaria__suficiente_alimento=obj[0]).count()
        grafo_suficiente_alimento[obj[1]] =  valor

    grafo_consumo_diario = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(seguridadalimentaria__consumo_diario=obj[0]).count()
        grafo_consumo_diario[obj[1]] =  valor


    conteo_fenomeno = {}
    for obj in CHOICE_FENOMENOS:
        valor = Encuesta.objects.filter(respuestano41__fenomeno=obj[0]).count()
        conteo_fenomeno[obj[1]] =  valor

    conteo_agricola = {}
    for obj in CHOICE_AGRICOLA:
        valor = Encuesta.objects.filter(respuestano41__agricola=obj[0]).count()
        conteo_agricola[obj[1]] =  valor

    conteo_mercado = {}
    for obj in CHOICE_MERCADO:
        valor = Encuesta.objects.filter(respuestano41__mercado=obj[0]).count()
        conteo_mercado[obj[1]] =  valor

    conteo_inversion = {}
    for obj in CHOICE_INVERSION:
        valor = Encuesta.objects.filter(respuestano41__inversion=obj[0]).count()
        conteo_inversion[obj[1]] =  valor

    grafo_adquiere_agua = {}
    for obj in AdquiereAgua.objects.all():
        valor = Encuesta.objects.filter(otrasseguridad__adquiere_agua=obj).count()
        grafo_adquiere_agua[obj] =  valor

    grafo_tratamiento_agua = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(otrasseguridad__tratamiento=obj[0]).count()
        grafo_tratamiento_agua[obj[1]] =  valor

    grafo_tipo_tratamientos = {}
    for obj in TrataAgua.objects.all():
        valor = Encuesta.objects.filter(otrasseguridad__tipo_tratamiento=obj).count()
        grafo_tipo_tratamientos[obj] =  valor

    return render(request, template, locals())

def genero(request, template="indicadores/genero.html"):

    #promedio de manzanas por todas las personas
    promedio_mz = Encuesta.objects.aggregate(p=Avg('organizacionfinca__area_finca'))['p']

    grafo_credito_mujer = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(genero1__tipo=obj[0]).count()
        grafo_credito_mujer[obj[1]] =  valor

    grafo_bienes_mujer = {}
    for obj in CHOICER_COSAS_MUJER:
        valor_si = Encuesta.objects.filter(genero2__pregunta=obj[0], genero2__respuesta=1).count()
        valor_no = Encuesta.objects.filter(genero2__pregunta=obj[0], genero2__respuesta=2).count()
        grafo_bienes_mujer[obj[1]] =  (valor_si, valor_no)

    grafo_organizacion_mujer = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(genero3__respuesta=obj[0]).count()
        grafo_organizacion_mujer[obj[1]] =  valor

    return render(request, template, locals())

#FUNCIONES UTILITARIAS
def saca_porcentajes(dato, total, formato=True):
    if dato != None:
        try:
            porcentaje = (dato/float(total)) * 100 if total != None or total != 0 else 0
        except:
            return 0
        if formato:
            return porcentaje
        else:
            return '%.2f' % porcentaje
    else:
        return 0
