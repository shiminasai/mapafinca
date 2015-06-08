from django.contrib import admin
from .models import *

class InlineDuenoSi(admin.TabularInline):
	model = DuenoSi

class InlineDuenoNo(admin.TabularInline):
	model = DuenoNo

class InlineSexoMiembros(admin.TabularInline):
	model = SexoMiembros

class InlineDetalleMiembros(admin.TabularInline):
	model = DetalleMiembros

class InlineEscolaridad(admin.TabularInline):
	model = Escolaridad

class AdminEncuesta(admin.ModelAdmin):
	inlines = [InlineDuenoSi,InlineDuenoNo,InlineSexoMiembros,
				InlineDetalleMiembros,InlineEscolaridad]

# Register your models here.
admin.site.register(Encuestadores)
admin.site.register(OrganizacionResp)
admin.site.register(Entrevistados)
admin.site.register(Encuesta, AdminEncuesta)
#admin.site.register()