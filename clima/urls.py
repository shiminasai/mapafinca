from django.conf.urls import url
from clima import views

urlpatterns = [
    url(r'^info-kcal-pais/$', views.info_consumo_kcal_pais, name='calorias-pais'),
    #url(r'^dashboard-principal/(?P<departamento_id>[0-9]+)/$', views.principal_dashboard, name='dashboard'),
    #url(r'^dashboard-principal-pais/(?P<pais>[-_\w]+)/$', views.principal_dashboard_pais, name='dashboard-pais'),
   
]