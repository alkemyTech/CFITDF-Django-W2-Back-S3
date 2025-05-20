from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Servicio

# Create your views here.

# Servicios
class ServicioCreateView(CreateView):
    model = Servicio
    template_name = 'editar.html'
    fields = '__all__'
    success_url = reverse_lazy('WebApp:servicio_listar')

    # Esto permite personalizar el contexto que se pasa a la plantilla.
    # De esta manera, editar.html puede ser usado tanto para crear como
    # para editar, dependiendo de la vista que lo llame.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_vista"] = "Crear Servicio"
        return context
    

class ServicioDetailView(DetailView):
    model = Servicio
    template_name = 'servicios/detalle.html'
    context_object_name = 'servicio'


class ServicioListView(ListView):
    model = Servicio
    template_name = 'servicios/listar.html'
    context_object_name = 'listado_servicios'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["listando_inactivos"] = self.kwargs.get('inactivos', False)
        return context
    
    def get_queryset(self):
        # Filtra servicios activos por defecto, pero permite listar inactivos
        # si se pasa 'inactivos' en la URL
        queryset = super().get_queryset()
        if self.kwargs.get('inactivos', False):
            return queryset.filter(activo=False)
        return queryset.filter(activo=True)
    

class ServicioUpdateView(UpdateView):
    model = Servicio
    template_name = 'editar.html'
    fields = '__all__'
    success_url = reverse_lazy('WebApp:servicio_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_vista"] = "Modificar Servicio"
        return context
    

def servicio_cambiar_estado(request, pk):
    servicio = get_object_or_404(Servicio, id=pk)
    servicio.activo = not servicio.activo
    servicio.save()
    return HttpResponseRedirect(reverse_lazy('WebApp:servicio_listar'))

# Clientes