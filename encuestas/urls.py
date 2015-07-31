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
]
