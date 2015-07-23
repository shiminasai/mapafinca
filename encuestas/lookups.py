from selectable.base import ModelLookup
from selectable.registry import registry
from .models import Entrevistados

class ProductorLookup(ModelLookup):
    model = Entrevistados
    search_fields = ('nombre__icontains', )
    #filters = {'activo': 1, }

registry.register(ProductorLookup)