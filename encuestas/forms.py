# -*- coding: utf-8 -*-
from django import forms
from .models import *
from lookups import *
import selectable.forms as selectable

class ProductorAdminForm(forms.ModelForm):

    class Meta(object):
        model = Encuesta
        fields = '__all__'
        widgets = {
            'entrevistado': selectable.AutoCompleteSelectWidget(lookup_class=ProductorLookup),
        }

class TipoEnergiaForm(forms.ModelForm):
    class Meta:
        model = TipoEnergia
        fields = '__all__'
        widgets = {
            'tipo': forms.CheckboxSelectMultiple(attrs={'size':'10'})
        }

class EnergiaSolarCocinarForm(forms.ModelForm):
    class Meta:
        model = EnergiaSolarCocinar
        fields = '__all__'
        widgets = {
            'fuente': forms.CheckboxSelectMultiple(attrs={'size':'10'})
        }

class TipoCocinasForm(forms.ModelForm):
    class Meta:
        model = TipoCocinas
        fields = '__all__'
        widgets = {
            'cocina': forms.CheckboxSelectMultiple(attrs={'size':'10'})
        }

class AccesoAguaForm(forms.ModelForm):
    class Meta:
        model = AccesoAgua
        fields = '__all__'
        widgets = {
            'agua': forms.CheckboxSelectMultiple(attrs={'size':'10'})
        }

CHOICE_SEXO = (
                (1, 'Mujer'),
                (2, 'Hombre'),
              )

CHOICE_FECHA  = (
              (2015, '2015'),
              (2016, '2016'),
            )

class ConsultarForm(forms.Form):
    fecha = forms.MultipleChoiceField(choices=CHOICE_FECHA, label="Años")
    organizacion = forms.ModelMultipleChoiceField(queryset=OrganizacionResp.objects.all(), required=False)
    pais = forms.ModelChoiceField(queryset=Pais.objects.all(), required=True)
    departamento = forms.ModelMultipleChoiceField(queryset=Departamento.objects.filter(entrevistados__gt=1).distinct(), required=False)
    municipio = forms.ModelMultipleChoiceField(queryset=Municipio.objects.all(), required=False)
    comunidad = forms.ModelMultipleChoiceField(queryset=Comunidad.objects.all(), required=False)
    #sexo = forms.ChoiceField(choices=CHOICE_SEXO, required=False)
