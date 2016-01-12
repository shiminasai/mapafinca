from django.conf.urls import url
from encuestas import views

urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url(r'^mapa/$', views.MapaView.as_view(), name='mapa'),
    url(r'^primer_mapa/$', views.FirstMapaView.as_view(), name='primer-mapa'),
    url(r'^dashboard-principal/(?P<departamento_id>[0-9]+)/$', views.principal_dashboard, name='dashboard'),
    url(r'^finca/(?P<entrevistado_id>[0-9]+)/$', views.detalle_finca, name='detalle-finca'),
    url(r'^indicadores/$', views.indicadores, name='indicadores'),
    url(r'^mapa_dash/$', views.obtener_mapa_dashboard, name='obtener-lista'),
    url(r'^galeria/$', views.GalleryView.as_view(), name='galeria'),
    url(r'^detalle_indicador/$', views.DetailIndicadorView.as_view(), name='galeria'),
    #otros indicadores
    url(r'^jefe_sexo/$', views.sexo_duenos, name='jefe-sexo'),
    url(r'^escolaridad/$', views.escolaridad, name='escolaridad'),
    url(r'^energia/$', views.energia, name='energia'),
    url(r'^agua/$', views.agua, name='agua'),
    url(r'^organizaciones/$', views.organizaciones, name='organizaciones'),
    url(r'^tierra/$', views.tierra, name='tierra'),
    url(r'^prestamos/$', views.prestamos, name='prestamos'),
    url(r'^practicas/$', views.practicas, name='practicas'),
    url(r'^seguridad/$', views.seguridad, name='seguridad'),
    url(r'^genero/$', views.genero, name='genero'),
    url(r'^ingresos/$', views.ingresos, name='ingreso'),

]
