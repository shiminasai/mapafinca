from django.conf.urls import url
from encuestas import views

urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url(r'^mapa/$', views.MapaView.as_view(), name='mapa'),
    url(r'^dashboard-principal/(?P<departamento_id>[0-9]+)/$', views.principal_dashboard, name='dashboard'),
    url(r'^finca/(?P<entrevistado_id>[0-9]+)/$', views.detalle_finca, name='detalle-finca'),

]