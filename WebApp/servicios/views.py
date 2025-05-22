# Create your views here.
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Servicio, Coordinador, ReservaServicio, Cliente
from .forms import ReservaServicioForm 

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
    
# Si alguien conoce una forma más elegante de hacer esto, por favor
# háganmelo saber
def servicio_cambiar_estado(request, pk):
    servicio = get_object_or_404(Servicio, id=pk)
    servicio.activo = not servicio.activo
    servicio.save()
    return HttpResponseRedirect(reverse_lazy('WebApp:servicio_listar'))

# Cliente
class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'editar.html'
    fields = '__all__'
    success_url = reverse_lazy('WebApp:cliente_crear')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_vista"] = "Crear Cliente"
        return context

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente/detalle.html'
    context_object_name = 'cliente'

class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente/listar.html'
    context_object_name = 'listado_clientes'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["listando_inactivos"] = self.kwargs.get('inactivos', False)
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.kwargs.get('inactivos', False):
            return queryset.filter(activo=False)
        return queryset.filter(activo=True)
    
# Coordinador
class CoordinadorCreateView(CreateView):
    model = Coordinador
    template_name = 'editar.html'
    fields = '__all__'
    success_url = reverse_lazy('WebApp:coordinador_crear')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_vista"] = "Crear Coordinador"
        return context
    
class CoordinadorDetailView(DetailView):
    model = Coordinador
    template_name = 'coordinador/detalle.html'
    context_object_name = 'coordinador'


class CoordinadorListView(ListView):
    model = Coordinador
    template_name = 'coordinador/listar.html'
    context_object_name = 'listado_coordinador'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["listando_inactivos"] = self.kwargs.get('inactivos',False)
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.kwargs.get('inactivos', False):
            return queryset.filter(activo=False)
        return queryset.filter(activo=True)
    
    
# ReservaServicio
class ReservaServicioCreateView(CreateView):
    model = ReservaServicio
    template_name = 'editar.html'
    form_class = ReservaServicioForm 
    success_url = reverse_lazy('WebApp:reserva_servicio_crear')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_vista"] = "Crear Reserva"
        return context
    

class ReservaServicioDetailView(DetailView):
    model = ReservaServicio
    template_name = 'servicios/detalle_reserva_servicio.html'
    context_object_name = 'reserva_servicio'


class ReservaServicioListView(ListView):
    model = ReservaServicio
    template_name = 'servicios/listar_reserva_servicio.html'
    context_object_name = 'listado_reservas_servicios'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["listando_inactivos"] = self.kwargs.get('inactivos', False)
        return context
    
    def get_queryset(self):
        return ReservaServicio.objects.all() 
    

class ReservaServicioUpdateView(UpdateView):
    model = ReservaServicio
    template_name = 'editar.html'
    form_class = ReservaServicioForm 
    success_url = reverse_lazy('WebApp:reserva_servicio_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_vista"] = "Modificar Reserva"
        return context
    

class ReservaServicioDeleteView(DeleteView):
    model = ReservaServicio
    success_url = reverse_lazy("WebApp:reserva_servicio_listar")
    template_name = "servicios/borrar.html"  
    

