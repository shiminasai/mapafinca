from django import template
import locale
register = template.Library()

@register.filter(name='calculaperct')
def calculaperct(value1, value2):
    try:
        resultado = (float(value1) / float(value2) * 100)
        return resultado
    except:
        return 0

@register.filter(name='calculaUtilidad')
def calculaUtilidad(value1, value2):
    try:
        resultado = float(value1) - float(value2)
        return resultado
    except:
        return 0

@register.filter(name='calculaSumatoriaIngreso')
def calculaSumatoriaIngreso(value1):
    try:
        resultado += float(value1)
        return resultado
    except:
        return 0

@register.filter(name='calcularIngresoXfamilia')
def calcularIngresoXfamilia(value1, value2):
    try:
        resultado = float(value1) / float(value2)
        return resultado
    except:
        return 0
