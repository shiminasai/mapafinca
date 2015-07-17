from django.conf.urls import url
from encuestas import views

urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url(r'^mapa/$', views.MapaView.as_view(), name='mapa'),
]