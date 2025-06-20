# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Servicio, Coordinador, ReservaServicio, Cliente, Empleado
from .forms import ReservaServicioForm, CoordinadorForm


def home(request):
    return render(request, 'home.html')

# Servicios
class ServicioCreateView(CreateView):
    model = Servicio
    template_name = 'servicios/editar.html'
    fields = '__all__'
    success_url = reverse_lazy('WebApp:servicio_crear')

    # Esto permite personalizar el contexto que se pasa a la plantilla.
    # De esta manera, editar.html puede ser usado tanto para crear como
    # para editar, dependiendo de la vista que lo llame.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_vista"] = "Crear Servicio"
        return context
    
    def form_valid(self, form):
        return super().form_valid(form)
    

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
    template_name = 'servicios/editar.html'
    fields = '__all__'
    success_url = reverse_lazy('WebApp:servicio_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_vista"] = "Modificar Servicio"
        return context
    
    def form_valid(self, form):
        return super().form_valid(form)
    
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
    template_name = 'cliente/editar.html'
    fields = '__all__'
    success_url = reverse_lazy('WebApp:cliente_crear')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_vista"] = "Crear Cliente"
        return context
    
    def form_valid(self, form):
        return super().form_valid(form)

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
      
      
class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'cliente/editar.html'
    fields = '__all__'
    success_url = reverse_lazy('WebApp:cliente_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_vista"] = "Modificar Cliente"
        return context
    
    def form_valid(self, form):
        return super().form_valid(form)
    

def cliente_cambiar_estado(request, pk):
    cliente = get_object_or_404(Cliente, id=pk)
    cliente.activo = not cliente.activo
    cliente.save()
    return HttpResponseRedirect(reverse_lazy('WebApp:cliente_listar'))
    
# Coordinador
class CoordinadorCreateView(CreateView):
    model = Coordinador
    template_name = 'coordinador/editar.html'
    form_class = CoordinadorForm
    success_url = reverse_lazy('WebApp:coordinador_crear')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_vista"] = "Crear Coordinador"
        return context
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    
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
    

class CoordinadorUpdateView(UpdateView):
    model = Coordinador
    template_name = 'coordinador/editar.html'
    form_class = CoordinadorForm
    success_url = reverse_lazy('WebApp:coordinador_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_vista"] = "Modificar Coordinador"
        return context
    
    def form_valid(self, form):
        return super().form_valid(form)
    

def coordinador_cambiar_estado(request, pk):
    coordinador = get_object_or_404(Coordinador, id=pk)
    coordinador.activo = not coordinador.activo
    coordinador.save()
    return HttpResponseRedirect(reverse_lazy('WebApp:coordinador_listar'))
    
    
# ReservaServicio
class ReservaServicioCreateView(CreateView):
    model = ReservaServicio
    template_name = 'reserva/editar.html'
    form_class = ReservaServicioForm 
    success_url = reverse_lazy('WebApp:reserva_servicio_crear')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_vista"] = "Crear Reserva"
        return context
    
    def form_valid(self, form):
        return super().form_valid(form)
    

class ReservaServicioDetailView(DetailView):
    model = ReservaServicio
    template_name = 'reserva/detalle.html'
    context_object_name = 'reserva_servicio'


class ReservaServicioListView(ListView):
    model = ReservaServicio
    template_name = 'reserva/listar.html'
    context_object_name = 'listado_reservas_servicios'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["listando_inactivos"] = self.kwargs.get('inactivos', False)
        return context
    
    def get_queryset(self):
        return ReservaServicio.objects.all() 
    

class ReservaServicioUpdateView(UpdateView):
    model = ReservaServicio
    template_name = 'reserva/editar.html'
    form_class = ReservaServicioForm 
    success_url = reverse_lazy('WebApp:reserva_servicio_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_vista"] = "Modificar Reserva"
        return context
    
    def form_valid(self, form):
        return super().form_valid(form)
    

class ReservaServicioDeleteView(DeleteView):
    model = ReservaServicio
    success_url = reverse_lazy("WebApp:reserva_servicio_listar")
    template_name = "reserva/borrar.html"  
    
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
    
    def form_valid(self, form):
        return super().form_valid(form)
    

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
        context["listando_inactivos"] = self.kwargs.get('inactivos', False)

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
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    
def empleado_cambiar_estado(request, pk):
    empleado = get_object_or_404(Empleado, id=pk)
    empleado.activo = not empleado.activo
    empleado.save()
    return HttpResponseRedirect(reverse_lazy('WebApp:empleado_listar'))

# Calendario

def calendario(request):
    return render(request, 'calendario.html')
