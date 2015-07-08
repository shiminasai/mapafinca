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

    list_display = ('entrevistado','dueno',)
    search_fields = ('entrevistado__nombre',)

    class Media:
        css = {
            "all": ("css/my_styles_admin.css",)
        }
        js = ("js/code_admin.js",)

class EntrevistadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'sexo', 'jefe', 'pais', 'departamento')
    list_filter = ('sexo','pais','departamento')
    search_fields = ('nombre',)


# Register your models here.
admin.site.register(Encuestadores)
admin.site.register(OrganizacionResp)
admin.site.register(Entrevistados, EntrevistadoAdmin)
admin.site.register(Encuesta, AdminEncuesta)
#admin.site.register()