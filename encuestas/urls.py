from django.conf.urls import url
from encuestas import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]