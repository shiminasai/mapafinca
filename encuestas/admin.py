from django.contrib import admin
from .models import *

class InlineDuenoSi(admin.TabularInline):
	model = DuenoSi
	extra = 1
	max_num = 1

class InlineDuenoNo(admin.TabularInline):
	model = DuenoNo
	extra = 1
	max_num = 1

class InlineSexoMiembros(admin.TabularInline):
	model = SexoMiembros
	extra = 1

class InlineDetalleMiembros(admin.TabularInline):
	model = DetalleMiembros
	extra = 1

class InlineEscolaridad(admin.TabularInline):
	model = Escolaridad
	extra = 1

class AdminEncuesta(admin.ModelAdmin):
	inlines = [InlineDuenoSi,InlineDuenoNo,InlineSexoMiembros,
				InlineDetalleMiembros,InlineEscolaridad]

# Register your models here.
admin.site.register(Encuestadores)
admin.site.register(OrganizacionResp)
admin.site.register(Entrevistados)
admin.site.register(Encuesta, AdminEncuesta)
#admin.site.register()