# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.views.generic import TemplateView
from .forms import ConsultarForm
from .models import *
import json as simplejson
from django.db.models import Sum, Avg, Value as V
from clima.models import *
from collections import OrderedDict
from django.db.models import Q
from django.db.models.functions import Coalesce
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
            for mun in Departamento.objects.all():
                m = Encuesta.objects.filter(entrevistado__departamento=mun, entrevistado__pais=pais).count()
                if m > 0:
                    paises[pais][mun.nombre] = (m,mun.id)

    return render(request, template, locals())


def obtener_mapa_dashboard(request):
    if request.is_ajax():
        lista = []
        for objeto in Encuesta.objects.filter(entrevistado__departamento=request.session['departamento']).distinct('entrevistado_id'):
            if objeto.entrevistado.longitud != None and objeto.entrevistado.longitud != '':
                dicc = dict(nombre=objeto.entrevistado.nombre,
                            id=objeto.entrevistado.id,
                            lon=float(objeto.entrevistado.longitud),
                            lat=float(objeto.entrevistado.latitud),
                            finca=objeto.entrevistado.finca,
                            comunidad=objeto.entrevistado.comunidad.nombre,
                            sexo=objeto.entrevistado.get_sexo_display(),
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

def principal_dashboard(request, template='dashboard.html', departamento_id=None,):
    #a = _queryset_filtrado(request)
    ahora = Encuesta.objects.filter(entrevistado__departamento=departamento_id).distinct('entrevistado__id')
    dividir_todo = len(ahora)
    depart = Departamento.objects.get(id=departamento_id)
    request.session['departamento'] = depart
    request.session['pais'] = depart.pais
    request.session['encuestados'] = dividir_todo

    geolat = []
    geolong = []
    for obj in depart.municipio_set.all():
        geolat.append(obj.latitud)
        geolong.append(obj.longitud)

    latitud = geolat[-1]
    longitud = geolong[-1]

    # grafico de patron de gastos
    try:
        gasto_finca = float(Encuesta.objects.filter(entrevistado__departamento=departamento_id,gastohogar__tipo=5).aggregate(t=Sum('gastohogar__total'))['t'] / 12) / float(dividir_todo)
    except:
        pass
    try:
        gasto_fuera_finca = float(Encuesta.objects.filter(entrevistado__departamento=departamento_id).aggregate(t=Sum('gastoproduccion__total'))['t'] / 12) / float(dividir_todo)
    except:
        pass
    # grafico de ingresos
    try:
        tradicional = float(Encuesta.objects.filter(entrevistado__departamento=departamento_id).aggregate(t=Sum('cultivostradicionales__total'))['t'] / 12) / float(dividir_todo)
    except:
        pass

    try:
        huertos = float(Encuesta.objects.filter(entrevistado__departamento=departamento_id).aggregate(t=Sum('cultivoshuertosfamiliares__total'))['t'] / 12) / float(dividir_todo)
    except:
        pass

    try:
        frutas = float(Encuesta.objects.filter(entrevistado__departamento=departamento_id).aggregate(t=Sum('cultivosfrutasfinca__total'))['t'] / 12 ) / float(dividir_todo)
    except:
        pass

    try:
        fuente = float(Encuesta.objects.filter(entrevistado__departamento=departamento_id).aggregate(t=Sum('fuentes__total'))['t'] / 12) / float(dividir_todo)
    except:
        pass

    try:
        ganado = float(Encuesta.objects.filter(entrevistado__departamento=departamento_id).aggregate(t=Sum('ganaderia__total'))['t'] / 12) / float(dividir_todo)
    except:
        pass

    try:
        procesamiento = float(Encuesta.objects.filter(entrevistado__departamento=departamento_id).aggregate(t=Sum('procesamiento__total'))['t'] / 12) / float(dividir_todo)
    except:
        pass

    #grafico de kcalorias aun esta en proceso

    #grafico sobre gastos alimentarios
    gastos_alimentarios = {}
    for obj in ProductosFueraFinca.objects.all():
        try:
            cada_uno = float(Encuesta.objects.filter(entrevistado__departamento=departamento_id, alimentosfuerafinca__producto=obj).aggregate(t=Avg('alimentosfuerafinca__total'))['t'] / 12) / float(dividir_todo)
        except:
            pass
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

    # grafico  de tela de araña : capital natural
    capital_natural_mujer = Encuesta.objects.filter(entrevistado__departamento=departamento_id, sexomiembros__sexo=1, dueno=1).count()
    capital_natural_hombre = Encuesta.objects.filter(entrevistado__departamento=departamento_id, sexomiembros__sexo=2, dueno=1).count()
    capital_natural_ambos = Encuesta.objects.filter(entrevistado__departamento=departamento_id, sexomiembros__sexo=3, dueno=1).count()
    #capital social
    capital_social_mujer = Encuesta.objects.filter(entrevistado__departamento=departamento_id, sexomiembros__sexo=1, organizacioncomunitaria__pertenece=1).count()
    capital_social_hombre = Encuesta.objects.filter(entrevistado__departamento=departamento_id, sexomiembros__sexo=2, organizacioncomunitaria__pertenece=1).count()
    capital_social_ambos = Encuesta.objects.filter(entrevistado__departamento=departamento_id, sexomiembros__sexo=3, organizacioncomunitaria__pertenece=1).count()
    #capital financiero
    capital_financiero_mujer = Encuesta.objects.filter(entrevistado__departamento=departamento_id, sexomiembros__sexo=1, totalingreso__total__gt=1).count()
    capital_financiero_hombre = Encuesta.objects.filter(entrevistado__departamento=departamento_id, sexomiembros__sexo=2, totalingreso__total__gt=1).count()
    capital_financiero_ambos = Encuesta.objects.filter(entrevistado__departamento=departamento_id, sexomiembros__sexo=3, totalingreso__total__gt=1).count()
    #capital fisico
    capital_fisico_mujer = Encuesta.objects.filter(Q(entrevistado__departamento=departamento_id), Q(sexomiembros__sexo=1), Q(totalingreso__total__gt=1) |  Q(tipoenergia__tipo=4)).count()
    capital_fisico_hombre = Encuesta.objects.filter(Q(entrevistado__departamento=departamento_id), Q(sexomiembros__sexo=2), Q(totalingreso__total__gt=1) |  Q(tipoenergia__tipo=4)).count()
    capital_fisico_ambos = Encuesta.objects.filter(Q(entrevistado__departamento=departamento_id), Q(sexomiembros__sexo=3), Q(totalingreso__total__gt=1) |  Q(tipoenergia__tipo=4)).count()
    #capital humano
    capital_humano_mujer = Encuesta.objects.filter(Q(entrevistado__departamento=departamento_id), Q(sexomiembros__sexo=1),
                                                                                    Q(escolaridad__secu_incompleta__gt=1) |  Q(escolaridad__bachiller__gt=1) |  Q(escolaridad__uni_tecnico__gt=1)).count()
    capital_humano_hombre = Encuesta.objects.filter(Q(entrevistado__departamento=departamento_id), Q(sexomiembros__sexo=2),
                                                                                    Q(escolaridad__secu_incompleta__gt=1) |  Q(escolaridad__bachiller__gt=1) |  Q(escolaridad__uni_tecnico__gt=1)).count()
    capital_humano_ambos = Encuesta.objects.filter(Q(entrevistado__departamento=departamento_id), Q(sexomiembros__sexo=3),
                                                                                    Q(escolaridad__secu_incompleta__gt=1) |  Q(escolaridad__bachiller__gt=1) |  Q(escolaridad__uni_tecnico__gt=1)).count()
    kcalorias = envio_calorias(request)

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
        #calculo ingreso vs gasto
        gasto_total = detalle.filter(year=year[0]).aggregate(t=Sum('totalingreso__total_gasto'))['t']
        gasto_total_fuera = detalle.filter(year=year[0]).aggregate(t=Sum('totalingreso__total_gasto_fuera_finca'))['t']

        ingreso_total = detalle.filter(year=year[0]).aggregate(t=Sum('totalingreso__total'))['t']
        total_gastos = gasto_total + gasto_total_fuera

        ingreso_cultivo_tradicional = {}
        for obj in Cultivos.objects.all():
            cultivo = CultivosTradicionales.objects.filter(encuesta__entrevistado__departamento=request.session['departamento'],
                                                            cultivo=obj, encuesta__entrevistado__id=entrevistado_id, encuesta__year=year[0])
            cosechada = cultivo.aggregate(t=Sum('cantidad_cosechada'))['t']
            venta = cultivo.aggregate(t=Sum('venta'))['t']
            precio = cultivo.aggregate(t=Avg('precio'))['t']
            try:
                ingreso = venta * precio
            except:
                ingreso = 0
            costo = cultivo.aggregate(t=Avg('costo'))['t']
            if venta > 0:
                ingreso_cultivo_tradicional[obj] = {'unidad':obj.get_unidad_medida_display(),
                                                'cantidad_cosechada':cosechada,
                                                'venta':venta,
                                                'precio':precio,
                                                'ingreso': ingreso,
                                                'costo':costo}

        ingreso_huertos = {}
        ingreso_patio = 0
        for obj in CultivosHuertos.objects.all():
            cultivo = CultivosHuertosFamiliares.objects.filter(cultivo=obj,
                                                            encuesta__entrevistado__id=entrevistado_id,
                                                            encuesta__year=year[0])
            print cultivo
            cosechada = cultivo.aggregate(t=Sum('cantidad_cosechada'))['t']
            venta = cultivo.aggregate(t=Sum('venta'))['t']
            precio = cultivo.aggregate(t=Avg('precio'))['t']
            try:
                ingreso = venta * precio
            except:
                ingreso = 0
            costo_huerto = CostoHuerto.objects.filter(encuesta__entrevistado__id=entrevistado_id,
                                                                                 encuesta__year=year[0]).aggregate(t=Avg('costo'))['t']
            ingreso_patio += ingreso

            if venta > 0:
                ingreso_huertos[obj] = {'unidad':obj.get_unidad_medida_display(),
                                                'cantidad_cosechada':cosechada,
                                                'venta':venta,
                                                'precio':precio,
                                                'ingreso': ingreso,
                                                }

        gran_dicc[year[1]] = (ingreso_total, total_gastos,ingreso_cultivo_tradicional, ingreso_huertos)

    return render(request, template, locals())


def indicadores(request, template='indicadores.html'):
    #a = _queryset_filtrado(request)
    #indicadores = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento']).distinct('entrevistado__id')
    total_entrevistados = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento']).distinct('entrevistado__id').count()
    total_hombres = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], entrevistado__sexo=2).distinct('entrevistado__id').count()
    total_mujeres = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], entrevistado__sexo=1).distinct('entrevistado__id').count()

    porcentaje_hombres = float(total_hombres) / float(total_entrevistados) * 100
    porcentaje_mujeres = float(total_mujeres) / float(total_entrevistados) * 100

    organizaciones = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento']).distinct('entrevistado__departamento').count()
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


def indicadores1(request, template='indicadores1.html'):
    total_entrevistados = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento']).distinct('entrevistado__id').count()
    total_hombres = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], entrevistado__sexo=2).distinct('entrevistado__id').count()
    total_mujeres = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], entrevistado__sexo=1).distinct('entrevistado__id').count()

    porcentaje_hombres = float(total_hombres) / float(total_entrevistados) * 100
    porcentaje_mujeres = float(total_mujeres) / float(total_entrevistados) * 100

    organizaciones = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento']).distinct('entrevistado__departamento').count()
    familias = Entrevistados.objects.count()
    return render(request, template, locals())

#FUNCIONES PARA LAS DEMAS SALIDAS DEL SISTEMA

def sexo_duenos(request, template="indicadores/sexo_duenos.html"):

    years = []
    for en in Encuesta.objects.order_by('year').values_list('year', flat=True):
        years.append((en,en))
    list(set(years))

    dicc_sexo_dueno = OrderedDict()
    for year in years:

        si_dueno = Encuesta.objects.filter(year=year[0],entrevistado__departamento=request.session['departamento'], dueno=1).count()
        no_dueno = Encuesta.objects.filter(year=year[0],entrevistado__departamento=request.session['departamento'], dueno=2).count()

        a_nombre = {}
        for obj in CHOICE_DUENO_SI:
            conteos = Encuesta.objects.filter(year=year[0],entrevistado__departamento=request.session['departamento'], duenosi__si=obj[0]).count()
            a_nombre[obj[1]] = conteos

        situacion = {}
        for obj in CHOICE_DUENO_NO:
            conteos = Encuesta.objects.filter(year=year[0],entrevistado__departamento=request.session['departamento'], duenono__no=obj[0]).count()
            situacion[obj[1]] = conteos

        sexo_jefe_hogar = {}
        for obj in CHOICE_SEXO:
            conteos = Encuesta.objects.filter(year=year[0],entrevistado__departamento=request.session['departamento'], sexomiembros__sexo=obj[0]).count()
            sexo_jefe_hogar[obj[1]] = conteos

        personas_habitan = {}
        for obj in CHOICE_SEXO:
            conteos = Encuesta.objects.filter(year=year[0],entrevistado__departamento=request.session['departamento'], sexomiembros__sexo=obj[0]).aggregate(t=Sum('sexomiembros__cantidad'))['t']
            personas_habitan[obj[1]] = conteos

        detalle_edad = {}
        for obj in CHOICE_EDAD:
            conteos = Encuesta.objects.filter(year=year[0],entrevistado__departamento=request.session['departamento'], detallemiembros__edad=obj[0]).aggregate(t=Sum('detallemiembros__cantidad'))['t']
            detalle_edad[obj[1]] = conteos

        dicc_sexo_dueno[year[1]] = (si_dueno,no_dueno,a_nombre,situacion,sexo_jefe_hogar,personas_habitan,detalle_edad)

    return render(request, template, locals())

def escolaridad(request, template="indicadores/escolaridad.html"):
    #filtro = _queryset_filtrado(request)

    years = []
    for en in Encuesta.objects.order_by('year').values_list('year', flat=True):
        years.append((en,en))
    list(set(years))

    dicc_escolaridad = OrderedDict()
    for year in years:

        tabla_educacion_hombre = []
        grafo_hombre = []
        suma_hombre = 0
        for e in CHOICE_ESCOLARIDAD:
            objeto = Encuesta.objects.filter(year=year[0],entrevistado__departamento=request.session['departamento'], escolaridad__sexo = e[0], entrevistado__sexo=2, entrevistado__jefe=1).aggregate(num_total = Sum('escolaridad__total'),
                    no_leer = Sum('escolaridad__no_leer'),
                    p_incompleta = Sum('escolaridad__pri_incompleta'),
                    p_completa = Sum('escolaridad__pri_completa'),
                    s_incompleta = Sum('escolaridad__secu_incompleta'),
                    bachiller = Sum('escolaridad__bachiller'),
                    universitario = Sum('escolaridad__uni_tecnico'),

                    )
            try:
                suma_hombre = int(objeto['p_completa'] or 0) + int(objeto['s_incompleta'] or 0) + int(objeto['bachiller'] or 0) + int(objeto['universitario'] or 0)
            except:
                pass
            variable = round(saca_porcentajes(suma_hombre,objeto['num_total']))
            grafo_hombre.append([e[1],variable])
            fila = [e[1], objeto['num_total'],
                    saca_porcentajes(objeto['no_leer'], objeto['num_total'], False),
                    saca_porcentajes(objeto['p_incompleta'], objeto['num_total'], False),
                    saca_porcentajes(objeto['p_completa'], objeto['num_total'], False),
                    saca_porcentajes(objeto['s_incompleta'], objeto['num_total'], False),
                    saca_porcentajes(objeto['bachiller'], objeto['num_total'], False),
                    saca_porcentajes(objeto['universitario'], objeto['num_total'], False),
                    ]
            tabla_educacion_hombre.append(fila)

            #tabla para cuando la mujer es jefe

        tabla_educacion_mujer = []
        grafo_mujer = []
        suma_mujer = 0
        for e in CHOICE_ESCOLARIDAD:
            objeto = Encuesta.objects.filter(year=year[0],entrevistado__departamento=request.session['departamento'], escolaridad__sexo = e[0], entrevistado__sexo=1, entrevistado__jefe=1).aggregate(num_total = Sum('escolaridad__total'),
                    no_leer = Sum('escolaridad__no_leer'),
                    p_incompleta = Sum('escolaridad__pri_incompleta'),
                    p_completa = Sum('escolaridad__pri_completa'),
                    s_incompleta = Sum('escolaridad__secu_incompleta'),
                    bachiller = Sum('escolaridad__bachiller'),
                    universitario = Sum('escolaridad__uni_tecnico'),

                    )
            try:
                suma_mujer = int(objeto['p_completa'] or 0) + int(objeto['s_incompleta'] or 0) + int(objeto['bachiller'] or 0) + int(objeto['universitario'] or 0)
            except:
                pass
            variable = round(saca_porcentajes(suma_mujer,objeto['num_total']))
            grafo_mujer.append([e[1],variable])
            fila = [e[1], objeto['num_total'],
                    saca_porcentajes(objeto['no_leer'], objeto['num_total'], False),
                    saca_porcentajes(objeto['p_incompleta'], objeto['num_total'], False),
                    saca_porcentajes(objeto['p_completa'], objeto['num_total'], False),
                    saca_porcentajes(objeto['s_incompleta'], objeto['num_total'], False),
                    saca_porcentajes(objeto['bachiller'], objeto['num_total'], False),
                    saca_porcentajes(objeto['universitario'], objeto['num_total'], False),
                    ]
            tabla_educacion_mujer.append(fila)
        dicc_escolaridad[year[1]] = (tabla_educacion_hombre,tabla_educacion_mujer)

    return render(request, template, locals())

def energia(request, template="indicadores/energia.html"):

    grafo_tipo_energia = {}
    for obj in Energia.objects.all():
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], tipoenergia__tipo=obj).count()
        grafo_tipo_energia[obj] =  valor

    grafo_panel_solar = {}
    for obj in CHOICE_PANEL_SOLAR:
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], panelsolar__panel=obj[0]).count()
        grafo_panel_solar[obj[1]] =  valor

    grafo_fuente_energia = {}
    for obj in FuenteEnergia.objects.all():
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], energiasolarcocinar__fuente=obj).count()
        grafo_fuente_energia[obj] =  valor

    grafo_tipo_cocina = {}
    for obj in Cocinas.objects.all():
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], tipococinas__cocina=obj).count()
        grafo_tipo_cocina[obj] =  valor


    return render(request, template, locals())

def agua(request, template="indicadores/agua.html"):

    grafo_agua_consumo = {}
    for obj in AguaConsumo.objects.all():
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], accesoagua__agua=obj).count()
        grafo_agua_consumo[obj] =  valor

    grafo_agua_disponibilidad = {}
    for obj in CHOICE_DISPONIBILIDAD:
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], disponibilidadagua__disponibilidad=obj[0]).count()
        grafo_agua_disponibilidad[obj[1]] =  valor

    grafo_agua_calidad = {}
    for obj in CHOICE_CALIDAD_AGUA:
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], calidadagua__calidad=obj[0]).count()
        grafo_agua_calidad[obj[1]] =  valor

    grafo_agua_contaminada = {}
    for obj in TipoContamindaAgua.objects.all():
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], contaminada__contaminada=obj).count()
        grafo_agua_contaminada[obj] =  valor

    grafo_agua_tratamiento = {}
    for obj in CHOICE_TRATAMIENTO:
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], tratamientoagua__tratamiento=obj[0]).count()
        grafo_agua_tratamiento[obj[1]] =  valor

    grafo_agua_usos = {}
    for obj in CHOICE_OTRO_USO:
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], usosagua__uso=obj[0]).count()
        grafo_agua_usos[obj[1]] =  valor


    return render(request, template, locals())

def organizaciones(request, template="indicadores/organizaciones.html"):

    grafo_pertenece = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], organizacioncomunitaria__pertenece=obj[0]).count()
        grafo_pertenece[obj[1]] =  valor

    grafo_org_comunitarias = {}
    for obj in OrgComunitarias.objects.all():
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], organizacioncomunitaria__caso_si=obj).count()
        if valor > 0:
            grafo_org_comunitarias[obj] =  valor

    grafo_beneficios = {}
    for obj in BeneficiosOrganizados.objects.all():
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], organizacioncomunitaria__cuales_beneficios=obj).count()
        if valor > 0:
            grafo_beneficios[obj] =  valor

    return render(request, template, locals())

def tierra(request, template="indicadores/tierra.html"):

    #tabla distribucion de frecuencia
    uno_num = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], organizacionfinca__area_finca__range=(0.1,5.99)).count()
    seis_num = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], organizacionfinca__area_finca__range=(6,10.99)).count()
    diez_mas = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], organizacionfinca__area_finca__gt=11).count()

    #promedio de manzanas por todas las personas
    promedio_mz = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento']).aggregate(p=Avg('organizacionfinca__area_finca'))['p']

    grafo_distribucion_tierra = {}
    for obj in CHOICE_TIERRA:
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], distribuciontierra__tierra=obj[0]).count()
        grafo_distribucion_tierra[obj[1]] =  valor

    return render(request, template, locals())

def prestamos(request, template="indicadores/prestamo.html"):

    grafo_prestamo_sino = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], prestamo__algun_prestamo=obj[0]).count()
        grafo_prestamo_sino[obj[1]] =  valor

    grafo_recibe_prestamo = {}
    for obj in RecibePrestamo.objects.all():
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], prestamo__recibe=obj).count()
        if valor > 0:
            grafo_recibe_prestamo[obj] =  valor

    grafo_uso_prestamo = {}
    for obj in UsoPrestamo.objects.all():
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], prestamo__uso=obj).count()
        if valor > 0:
            grafo_uso_prestamo[obj] =  valor

    return render(request, template, locals())

def practicas(request, template="indicadores/practicas.html"):

    grafo_practicas_sino = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], practicasagroecologicas__si_no=obj[0]).count()
        grafo_practicas_sino[obj[1]] =  valor

    grafo_manejo = {}
    for obj in CHOICE_MANEJO:
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], practicasagroecologicas__manejo=obj[0]).count()
        grafo_manejo[obj[1]] =  valor

    grafo_traccion = {}
    for obj in CHOICE_TRACCION:
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], practicasagroecologicas__traccion=obj[0]).count()
        grafo_traccion[obj[1]] =  valor

    grafo_fertilidad = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], practicasagroecologicas__fertilidad=obj[0]).count()
        grafo_fertilidad[obj[1]] =  valor

    grafo_control = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], practicasagroecologicas__control=obj[0]).count()
        grafo_control[obj[1]] =  valor

    return render(request, template, locals())

def seguridad(request, template="indicadores/seguridad.html"):

    grafo_economico = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], seguridadalimentaria__economico=obj[0]).count()
        grafo_economico[obj[1]] =  valor

    grafo_secado = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], seguridadalimentaria__secado=obj[0]).count()
        grafo_secado[obj[1]] =  valor

    grafo_tipo_secado = {}
    for obj in TipoSecado.objects.all():
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], seguridadalimentaria__tipo_secado=obj).count()
        grafo_tipo_secado[obj] =  valor

    grafo_plan_cosecha = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], seguridadalimentaria__plan_cosecha=obj[0]).count()
        grafo_plan_cosecha[obj[1]] =  valor

    grafo_ayuda = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], seguridadalimentaria__ayuda=obj[0]).count()
        grafo_ayuda[obj[1]] =  valor

    grafo_suficiente_alimento = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], seguridadalimentaria__suficiente_alimento=obj[0]).count()
        grafo_suficiente_alimento[obj[1]] =  valor

    grafo_consumo_diario = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], seguridadalimentaria__consumo_diario=obj[0]).count()
        grafo_consumo_diario[obj[1]] =  valor


    conteo_fenomeno = {}
    for obj in CHOICE_FENOMENOS:
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], respuestano41__fenomeno=obj[0]).count()
        conteo_fenomeno[obj[1]] =  valor

    conteo_agricola = {}
    for obj in CHOICE_AGRICOLA:
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], respuestano41__agricola=obj[0]).count()
        conteo_agricola[obj[1]] =  valor

    conteo_mercado = {}
    for obj in CHOICE_MERCADO:
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], respuestano41__mercado=obj[0]).count()
        conteo_mercado[obj[1]] =  valor

    conteo_inversion = {}
    for obj in CHOICE_INVERSION:
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], respuestano41__inversion=obj[0]).count()
        conteo_inversion[obj[1]] =  valor

    grafo_adquiere_agua = {}
    for obj in AdquiereAgua.objects.all():
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], otrasseguridad__adquiere_agua=obj).count()
        grafo_adquiere_agua[obj] =  valor

    grafo_tratamiento_agua = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], otrasseguridad__tratamiento=obj[0]).count()
        grafo_tratamiento_agua[obj[1]] =  valor

    grafo_tipo_tratamientos = {}
    for obj in TrataAgua.objects.all():
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], otrasseguridad__tipo_tratamiento=obj).count()
        grafo_tipo_tratamientos[obj] =  valor

    return render(request, template, locals())

def genero(request, template="indicadores/genero.html"):

    porcentaje_aporta_mujer = OrderedDict()
    for obj in CHOICER_INGRESO:
        porcentaje_aporta_mujer[obj[1]] = OrderedDict()
        for obj2 in CHOICE_PORCENTAJE:
            valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], genero__tipo=obj[0], genero__porcentaje=obj2[0]).count()
            if valor > 0:
                porcentaje_aporta_mujer[obj[1]][obj2[1]] =  valor


    grafo_credito_mujer = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], genero1__tipo=obj[0]).count()
        grafo_credito_mujer[obj[1]] =  valor

    grafo_bienes_mujer = {}
    for obj in CHOICER_COSAS_MUJER:
        valor_si = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], genero2__pregunta=obj[0], genero2__respuesta=1).count()
        valor_no = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], genero2__pregunta=obj[0], genero2__respuesta=2).count()
        grafo_bienes_mujer[obj[1]] =  (valor_si, valor_no)

    grafo_organizacion_mujer = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], genero3__respuesta=obj[0]).count()
        grafo_organizacion_mujer[obj[1]] =  valor

    mujer_organizacion = {}
    for obj in OrgComunitarias.objects.all():
        dato = OrganizacionComunitaria.objects.filter(encuesta__entrevistado__departamento=request.session['departamento'],
                                                    caso_si=obj, encuesta__entrevistado__jefe=1).count()
        mujer_organizacion[obj] = dato


    nivel_educacion_mujer = {}
    for obj in CHOICER_NIVEL_MUJER:
        valor = Genero4.objects.filter(encuesta__entrevistado__departamento=request.session['departamento'],
                                        opcion=obj[0]).count()
        nivel_educacion_mujer[obj[1]] =  valor

    divisor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento']).distinct('entrevistado__id').count()

    return render(request, template, locals())

def ingresos(request, template="indicadores/ingresos.html"):

    #años de encuestas
    years = []
    for en in Encuesta.objects.filter(entrevistado__departamento=request.session['departamento']).order_by('year').values_list('year', flat=True):
        years.append((en,en))
    list(set(years))

    percibe_ingreso = {}
    for obj in CHOICE_JEFE:
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], percibeingreso__si_no=obj[0]).count()
        percibe_ingreso[obj[1]] =  valor

    fuente_ingresos = {}
    for obj in TipoFuenteIngreso.objects.all():
        valor = Encuesta.objects.filter(entrevistado__departamento=request.session['departamento'], fuentes__fuente_ingreso=obj).count()
        fuente_ingresos[obj] =  valor

    #ingreso de cultivos tracionales

    ingreso_cultivo_tradicional = {}
    for obj in Cultivos.objects.all():
        cultivo = CultivosTradicionales.objects.filter(encuesta__entrevistado__departamento=request.session['departamento'],
                                                        cultivo=obj)
        cosechada = cultivo.aggregate(t=Sum('cantidad_cosechada'))['t']
        venta = cultivo.aggregate(t=Sum('venta'))['t']
        precio = cultivo.aggregate(t=Avg('precio'))['t']
        try:
            ingreso = venta * precio
        except:
            ingreso = 0
        costo = cultivo.aggregate(t=Avg('costo'))['t']
        if venta > 0:
            try:
                utilidad = ingreso - costo
            except:
                pass
            ingreso_cultivo_tradicional[obj] = {'unidad':obj.get_unidad_medida_display(),
                                            'cantidad_cosechada':cosechada,
                                            'venta':venta,
                                            'precio':precio,
                                            'ingreso': ingreso,
                                            'costo':costo,
                                            'utilidad': utilidad}

    total_utilidad_tradicional = sum(list([ i['utilidad'] for i in ingreso_cultivo_tradicional.values()]))
    total_ingreso_tradicional = sum(list([ i['ingreso'] for i in ingreso_cultivo_tradicional.values()]))
    total_costo_tradicional = sum(list([ i['costo'] for i in ingreso_cultivo_tradicional.values()]))
    #cultivos huertos familiares

    ingreso_huertos = {}
    ingreso_patio = 0
    for obj in CultivosHuertos.objects.all():
        cultivo = CultivosHuertosFamiliares.objects.filter(encuesta__entrevistado__departamento=request.session['departamento'],
                                                        cultivo=obj)
        cosechada = cultivo.aggregate(t=Sum('cantidad_cosechada'))['t']
        venta = cultivo.aggregate(t=Sum('venta'))['t']
        precio = cultivo.aggregate(t=Avg('precio'))['t']
        try:
            ingreso = venta * precio
        except:
            ingreso = 0
        costo_huerto = CostoHuerto.objects.filter(encuesta__entrevistado__departamento=request.session['departamento']).aggregate(t=Avg('costo'))['t']
        ingreso_patio += ingreso

        if venta > 0:
            ingreso_huertos[obj] = {'unidad':obj.get_unidad_medida_display(),
                                            'cantidad_cosechada':cosechada,
                                            'venta':venta,
                                            'precio':precio,
                                            'ingreso': ingreso,
                                            }
    utilidad_huerto_patio = ingreso_patio - costo_huerto
    # cultivos frutales

    ingreso_frutales = {}
    ingreso_fruta = 0
    for obj in CultivosFrutas.objects.all():
        cultivo = CultivosFrutasFinca.objects.filter(encuesta__entrevistado__departamento=request.session['departamento'],
                                                        cultivo=obj)
        cosechada = cultivo.aggregate(t=Sum('cantidad_cosechada'))['t']
        venta = cultivo.aggregate(t=Sum('venta'))['t']
        precio = cultivo.aggregate(t=Avg('precio'))['t']
        try:
            ingreso = venta * precio
        except:
            ingreso = 0
        costo_fruta = CostoFrutas.objects.filter(encuesta__entrevistado__departamento=request.session['departamento']).aggregate(t=Avg('costo'))['t']

        ingreso_fruta += ingreso
        if venta > 0:
            ingreso_frutales[obj] = {'unidad':obj.get_unidad_medida_display(),
                                            'cantidad_cosechada':cosechada,
                                            'venta':venta,
                                            'precio':precio,
                                            'ingreso': ingreso,
                                            }
    utilidad_frutas = ingreso_fruta - costo_fruta
    # animales en la finca

    ingreso_ganaderia = {}
    for obj in Animales.objects.all():
        cultivo = Ganaderia.objects.filter(encuesta__entrevistado__departamento=request.session['departamento'],
                                                        animal=obj)
        cantidad = cultivo.aggregate(t=Avg('cantidad'))['t']
        venta = cultivo.aggregate(t=Sum('cantidad_vendida'))['t']
        precio = cultivo.aggregate(t=Avg('precio'))['t']
        try:
            ingreso = venta * precio
        except:
            ingreso = 0

        if venta > 0:
            ingreso_ganaderia[obj] = {'cantidad':cantidad,
                                    'venta':venta,
                                    'precio':precio,
                                    'ingreso': ingreso,
                                    }

    total_ingreso_ganado = sum(list([ i['ingreso'] for i in ingreso_ganaderia.values()]))

    # comercializacion de productos procesados

    ingreso_procesado = {}
    for obj in ProductoProcesado.objects.all():
        cultivo = Procesamiento.objects.filter(encuesta__entrevistado__departamento=request.session['departamento'],
                                                        producto=obj)
        cantidad = cultivo.aggregate(t=Avg('cantidad_total'))['t']
        venta = cultivo.aggregate(t=Sum('cantidad_vendida'))['t']
        precio = cultivo.aggregate(t=Avg('precio'))['t']
        try:
            ingreso = venta * precio
        except:
            ingreso = 0

        if venta > 0:
            ingreso_procesado[obj] = {'unidad':obj.get_unidad_medida_display(),
                                    'cantidad':cantidad,
                                    'venta':venta,
                                    'precio':precio,
                                    'ingreso': ingreso,
                                    }
    total_ingreso_procesado = sum(list([ i['ingreso'] for i in ingreso_procesado.values()]))


    return render(request, template, locals())

def gastos(request, template="indicadores/gastos.html"):

    introducido_tradicional = {}
    for obj in Cultivos.objects.all():
        valor = IntroducidosTradicionales.objects.filter(encuesta__entrevistado__departamento=request.session['departamento'],
                                                        cultivo=obj,si_no=1).count()
        if valor > 0:
            introducido_tradicional[obj] =  valor

    introducido_huerto = {}
    for obj in CultivosHuertos.objects.all():
        valor = IntroducidosHuertos.objects.filter(encuesta__entrevistado__departamento=request.session['departamento'],
                                                        cultivo=obj,si_no=1).count()
        if valor > 0:
            introducido_huerto[obj] =  valor

    gasto_hogar = {}
    for obj in CHOICE_TIPO_GASTOS:
        valor = GastoHogar.objects.filter(encuesta__entrevistado__departamento=request.session['departamento'],
                                                    tipo=obj[0]).aggregate(t=Avg('cantidad'))['t']
        gasto_hogar[obj[1]] =  valor

    gasto_produccion = {}
    for obj in TipoGasto.objects.all():
        valor = GastoProduccion.objects.filter(encuesta__entrevistado__departamento=request.session['departamento'],
                                                        tipo=obj).aggregate(t=Avg('cantidad'))['t']
        gasto_produccion[obj] =  valor

    return render(request, template, locals())


def envio_calorias(request):
    calorias_tradicional = {}
    for obj in Cultivos.objects.all():
        calculo = CultivosTradicionales.objects.filter(encuesta__entrevistado__departamento=request.session['departamento'],
                                                                                cultivo=obj).aggregate(t=Coalesce(Avg('consumo_familia'), V(0)))['t']
        consumida = calculo * 12
        consumida_gramos = consumida * obj.calorias
        calorias_dia = float(consumida_gramos * obj.calorias) / 100
        gramo_dia = float(obj.proteinas*consumida_gramos) / 100
        if calorias_dia > 0:
            calorias_tradicional[obj] = (consumida, obj.get_unidad_medida_display(),consumida_gramos,obj.calorias, obj.proteinas,calorias_dia,gramo_dia)
    total_calorias_tradicional = sum(list([ i[5] for i in calorias_tradicional.values()]))
    total_proteina_tradicional = sum(list([ i[6] for i in calorias_tradicional.values()]))

    calorias_huerto = {}
    for obj in CultivosHuertos.objects.all():
        calculo = CultivosHuertosFamiliares.objects.filter(encuesta__entrevistado__departamento=request.session['departamento'],
                                                                                cultivo=obj).aggregate(t=Coalesce(Avg('consumo_familia'), V(0)))['t']
        consumida = calculo * 12
        consumida_gramos = consumida * obj.calorias
        calorias_dia = float(consumida_gramos * obj.calorias) / 100
        gramo_dia = float(obj.proteinas*consumida_gramos) / 100
        if calorias_dia > 0:
            calorias_huerto[obj] = (consumida, obj.get_unidad_medida_display(),consumida_gramos,obj.calorias, obj.proteinas,calorias_dia,gramo_dia)

    total_calorias_huerto = sum(list([ i[5] for i in calorias_huerto.values()]))
    total_proteina_huerto = sum(list([ i[6] for i in calorias_huerto.values()]))

    calorias_fruta = {}
    for obj in CultivosFrutas.objects.all():
        calculo = CultivosFrutasFinca.objects.filter(encuesta__entrevistado__departamento=request.session['departamento'],
                                                                                cultivo=obj).aggregate(t=Coalesce(Avg('consumo_familia'), V(0)))['t']
        consumida = calculo * 12
        consumida_gramos = consumida * obj.calorias
        calorias_dia = float(consumida_gramos * obj.calorias) / 100
        gramo_dia = float(obj.proteinas*consumida_gramos) / 100
        if calorias_dia > 0:
            calorias_fruta[obj] = (consumida, obj.get_unidad_medida_display(),consumida_gramos,obj.calorias, obj.proteinas,calorias_dia,gramo_dia)
    total_calorias_fruta = sum(list([ i[5] for i in calorias_fruta.values()]))
    total_proteina_fruta = sum(list([ i[6] for i in calorias_fruta.values()]))

    calorias_procesado = {}
    for obj in ProductoProcesado.objects.all():
        calculo = Procesamiento.objects.filter(encuesta__entrevistado__departamento=request.session['departamento'],
                                                                                producto=obj).aggregate(t=Coalesce(Avg('cantidad'), V(0)))['t']
        consumida = calculo * 12
        consumida_gramos = consumida * obj.calorias
        calorias_dia = float(consumida_gramos * obj.calorias) / 100
        gramo_dia = float(obj.proteinas*consumida_gramos) / 100
        if calorias_dia > 0:
            calorias_procesado[obj] = (consumida, obj.get_unidad_medida_display(),consumida_gramos,obj.calorias, obj.proteinas,calorias_dia,gramo_dia)

    total_calorias_procesado = sum(list([ i[5] for i in calorias_procesado.values()]))
    total_proteina_procesado = sum(list([ i[6] for i in calorias_procesado.values()]))

    calorias_fuera_finca = {}
    for obj in ProductosFueraFinca.objects.all():
        calculo = AlimentosFueraFinca.objects.filter(encuesta__entrevistado__departamento=request.session['departamento'],
                                                                                producto=obj).aggregate(t=Coalesce(Avg('cantidad'), V(0)))['t']
        consumida = calculo * 12
        consumida_gramos = consumida * obj.calorias
        calorias_dia = float(consumida_gramos * obj.calorias) / 100
        gramo_dia = float(obj.proteinas*consumida_gramos) / 100
        if calorias_dia > 0:
            calorias_fuera_finca[obj] = (consumida, obj.unidad_medida,consumida_gramos,obj.calorias, obj.proteinas,calorias_dia,gramo_dia)

    total_calorias_fuera_finca = sum(list([ i[5] for i in calorias_fuera_finca.values()]))
    total_proteina_fuera_finca = sum(list([ i[6] for i in calorias_fuera_finca.values()]))

    datos = {'Kcal Cultivos Tradicional':total_calorias_tradicional,
            'Kcal Huertos de patio':total_calorias_huerto,
            'Kcal Frutas':total_calorias_fruta,
            'Kcal Productos procesados':total_calorias_procesado,
            'Kcal Productos comprados': total_calorias_fuera_finca}
    return datos

def calorias(request, template="indicadores/calorias.html"):

    calorias_tradicional = {}
    for obj in Cultivos.objects.all():
        calculo = CultivosTradicionales.objects.filter(encuesta__entrevistado__departamento=request.session['departamento'],
                                                                                cultivo=obj).aggregate(t=Coalesce(Avg('consumo_familia'), V(0)))['t']
        consumida = calculo * 12
        consumida_gramos = consumida * obj.calorias
        calorias_dia = float(consumida_gramos * obj.calorias) / 100
        gramo_dia = float(obj.proteinas*consumida_gramos) / 100
        if calorias_dia > 0:
            calorias_tradicional[obj] = (consumida, obj.get_unidad_medida_display(),consumida_gramos,obj.calorias, obj.proteinas,calorias_dia,gramo_dia)
    total_calorias_tradicional = sum(list([ i[5] for i in calorias_tradicional.values()]))
    total_proteina_tradicional = sum(list([ i[6] for i in calorias_tradicional.values()]))

    calorias_huerto = {}
    for obj in CultivosHuertos.objects.all():
        calculo = CultivosHuertosFamiliares.objects.filter(encuesta__entrevistado__departamento=request.session['departamento'],
                                                                                cultivo=obj).aggregate(t=Coalesce(Avg('consumo_familia'), V(0)))['t']
        consumida = calculo * 12
        consumida_gramos = consumida * obj.calorias
        calorias_dia = float(consumida_gramos * obj.calorias) / 100
        gramo_dia = float(obj.proteinas*consumida_gramos) / 100
        if calorias_dia > 0:
            calorias_huerto[obj] = (consumida, obj.get_unidad_medida_display(),consumida_gramos,obj.calorias, obj.proteinas,calorias_dia,gramo_dia)

    total_calorias_huerto = sum(list([ i[5] for i in calorias_huerto.values()]))
    total_proteina_huerto = sum(list([ i[6] for i in calorias_huerto.values()]))

    calorias_fruta = {}
    for obj in CultivosFrutas.objects.all():
        calculo = CultivosFrutasFinca.objects.filter(encuesta__entrevistado__departamento=request.session['departamento'],
                                                                                cultivo=obj).aggregate(t=Coalesce(Avg('consumo_familia'), V(0)))['t']
        consumida = calculo * 12
        consumida_gramos = consumida * obj.calorias
        calorias_dia = float(consumida_gramos * obj.calorias) / 100
        gramo_dia = float(obj.proteinas*consumida_gramos) / 100
        if calorias_dia > 0:
            calorias_fruta[obj] = (consumida, obj.get_unidad_medida_display(),consumida_gramos,obj.calorias, obj.proteinas,calorias_dia,gramo_dia)
    total_calorias_fruta = sum(list([ i[5] for i in calorias_fruta.values()]))
    total_proteina_fruta = sum(list([ i[6] for i in calorias_fruta.values()]))

    calorias_procesado = {}
    for obj in ProductoProcesado.objects.all():
        calculo = Procesamiento.objects.filter(encuesta__entrevistado__departamento=request.session['departamento'],
                                                                                producto=obj).aggregate(t=Coalesce(Avg('cantidad'), V(0)))['t']
        consumida = calculo * 12
        consumida_gramos = consumida * obj.calorias
        calorias_dia = float(consumida_gramos * obj.calorias) / 100
        gramo_dia = float(obj.proteinas*consumida_gramos) / 100
        if calorias_dia > 0:
            calorias_procesado[obj] = (consumida, obj.get_unidad_medida_display(),consumida_gramos,obj.calorias, obj.proteinas,calorias_dia,gramo_dia)

    total_calorias_procesado = sum(list([ i[5] for i in calorias_procesado.values()]))
    total_proteina_procesado = sum(list([ i[6] for i in calorias_procesado.values()]))

    calorias_fuera_finca = {}
    for obj in ProductosFueraFinca.objects.all():
        calculo = AlimentosFueraFinca.objects.filter(encuesta__entrevistado__departamento=request.session['departamento'],
                                                                                producto=obj).aggregate(t=Coalesce(Avg('cantidad'), V(0)))['t']
        consumida = calculo * 12
        consumida_gramos = consumida * obj.calorias
        calorias_dia = float(consumida_gramos * obj.calorias) / 100
        gramo_dia = float(obj.proteinas*consumida_gramos) / 100
        if calorias_dia > 0:
            calorias_fuera_finca[obj] = (consumida, obj.unidad_medida,consumida_gramos,obj.calorias, obj.proteinas,calorias_dia,gramo_dia)

    total_calorias_fuera_finca = sum(list([ i[5] for i in calorias_fuera_finca.values()]))
    total_proteina_fuera_finca = sum(list([ i[6] for i in calorias_fuera_finca.values()]))

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
