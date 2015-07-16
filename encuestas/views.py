from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def _get_filtros(request):
	pass

#

class IndexView(TemplateView):
    template_name = "index.html"
