from django.contrib import admin
from .models import *

class TemperaturaAdmin(admin.ModelAdmin):
    list_display = ('pais','departamento','municipio','mes','year','temperatura')
    list_filter = ('pais','departamento',)
    search_fields = ('temperatura',)

class PrecipitacionAdmin(admin.ModelAdmin):
    list_display = ('pais','departamento','municipio','mes','year','precipitacion')
    list_filter = ('pais','departamento',)
    search_fields = ('precipitacion',)

# Register your models here.
admin.site.register(Precipitacion,PrecipitacionAdmin)
admin.site.register(Temperatura, TemperaturaAdmin)
admin.site.register(DiasEfectivoLLuvia)
