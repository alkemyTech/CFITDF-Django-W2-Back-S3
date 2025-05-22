from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy
from .models import Servicio, Coordinador

# Create your views here.

# Servicios
class ServicioCreateView(CreateView):
    model = Servicio
    template_name = 'editar.html'
    fields = '__all__'
    success_url = reverse_lazy('WebApp:servicio_crear')

    # Esto permite personalizar el contexto que se pasa a la plantilla.
    # De esta manera, editar.html puede ser usado tanto para crear como
    # para editar, dependiendo de la vista que lo llame.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_vista"] = "Crear Servicio"
        return context
    
# Coordinador CRUD

class CoordinadorCreateView(CreateView):
    model = Coordinador
    template_name = 'editar.html'
    fields = '__all__'
    success_url = reverse_lazy('WebApp:coordinador_crear')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_vista"] = "Crear Coordinador"
        return context