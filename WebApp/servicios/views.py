from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Empleado

# Create your views here.

# Empleado
class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'empleado/editar.html'
    fields = '__all__'
    success_url = reverse_lazy('WebApp:empleado_listar')

    # Esto permite personalizar el contexto que se pasa a la plantilla.
    # De esta manera, editar.html puede ser usado tanto para crear como
    # para editar, dependiendo de la vista que lo llame.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_vista"] = "Crear Empleado"
        return context
    

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado/detalle.html'
    context_object_name = 'empleado'


class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'empleado/listar.html'
    context_object_name = 'listado_empleado'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context["listando_inactivos"] = self.kwargs.get('inactivos', False)
        context["listando_inactivos"] = True
        return context
    
    def get_queryset(self):
        # Filtra empleados activos por defecto, pero permite listar inactivos
        # si se pasa 'inactivos' en la URL
        queryset = super().get_queryset()
        if self.kwargs.get('inactivos', False):
            return queryset.filter(activo=False)
        return queryset.filter(activo=True)
    

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = 'empleado/editar.html'
    fields = '__all__'
    success_url = reverse_lazy('WebApp:empleado_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_vista"] = "Modificar Empleado"
        return context
    

def empleado_cambiar_estado(request, pk):
    empleado = get_object_or_404(Empleado, id=pk)
    empleado.activo = not empleado.activo
    empleado.save()
    return HttpResponseRedirect(reverse_lazy('WebApp:empleado_listar'))