from django import forms
from .models import *

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

class ConsultarForm(forms.Form):
    sexo = forms.ChoiceField(choices=CHOICE_SEXO)
    organizacion = forms.ModelChoiceField(queryset=OrganizacionResp.objects.all())


