from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import ConsultarForm

# Create your views here.
def _queryset_filtrado(request):
	params = {}
	if request.session['sexo']:
		params['sexo'] = request.session['sexo']

	if request.session['organizacion']:
		params['organizacion'] = request.session['organizacion']

	unvalid_keys = []
	for key in params:
		if not params[key]:
			unvalid_keys.append(key)

	for key in unvalid_keys:
		del params[key]

	return Encuesta.objects.filter(**params)

def IndexView(request,template="index.html"):
	if request.method == 'POST':
		mensaje = None
		form = ConsultarForm(request.POST)
		if form.is_valid():
			request.session['sexo'] = form.cleaned_data['sexo']
			request.session['organizacion'] = form.cleaned_data['organizacion']
			mensaje = "Todas las variables estan correctamente :)"
			request.session['activo'] = True
			centinela = 1

			return redirect('/mapa/')

		else:
			centinela = 0   
		   
	else:
		form = ConsultarForm()
		mensaje = "Existen alguno errores"
		centinela = 0
		try:
			del request.session['sexo']
			del request.session['organizacion']
		except:
			pass

	return render(request, template, locals())

class MapaView(TemplateView):
    template_name = "mapa.html"