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
        context['elsalvado'] = 0#Encuesta.objects.filter(entrevistado__pais_id=2).count()
        context['honduras'] = 0#Encuesta.objects.filter(entrevistado__pais_id=3).count()
        context['guatemala'] = 0#Encuesta.objects.filter(entrevistado__pais_id=4).count()
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
    print gastos_alimentarios
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

    print porcentaje_mujeres

    #años que tiene ese productor
    years = []
    for en in Encuesta.objects.order_by('year').values_list('year', flat=True):
        years.append((en,en))
    list(set(years))

    #Ingresos por años
    ingreso_dicc = OrderedDict()
    for year in years:
        p = Procesamiento.objects.filter(encuesta__year=year[0]).aggregate(t=Sum('total'))['t']
        g = Ganaderia.objects.filter(encuesta__year=year[0]).aggregate(t=Sum('total'))['t']
        ch = CultivosHuertosFamiliares.objects.filter(encuesta__year=year[0]).aggregate(t=Sum('total'))['t']
        ct = CultivosTradicionales.objects.filter(encuesta__year=year[0]).aggregate(t=Sum('total'))['t']
        f = Fuentes.objects.filter(encuesta__year=year[0]).aggregate(t=Sum('total'))['t']
        cf = CultivosFrutasFinca.objects.filter(encuesta__year=year[0]).aggregate(t=Sum('total'))['t']

        ingreso_dicc[year[1]] = (p,g,ch,ct,f,cf)

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
