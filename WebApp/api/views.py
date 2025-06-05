#from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ServicioSerializer, CoordinadorSerializer, ClienteSerializer, EmpleadoSerializer
from servicios.models import Servicio, Coordinador, Cliente, Empleado, ReservaServicio

# Servicios
class ServicioListAPIView(ListAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

    def get_view_name(self):
        return "Lista de Servicios"


class ServicioRetrieveAPIView(RetrieveAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

    def get_view_name(self):
        return "Detalle de Servicio"
    
# Cliente
class ClienteListApiView(ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
    def get_view_name(self):
        return "Lista de Clientes"

class ClienteRetrieveAPIView(RetrieveAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get_view_name(self):
        return "Detalle de Cliente"
    
# Coordinadores
class CoordinadorAPIView(ListAPIView):
    queryset = Coordinador.objects.all()
    serializer_class = CoordinadorSerializer

class CoordinadorRetriveAPIView(RetrieveAPIView):
    queryset = Coordinador.objects.all()
    serializer_class = CoordinadorSerializer

    def get_view_name(self):
        return 'Detalle de Coordinador'

# Empleados
class EmpleadoListAPIView(ListAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

    def get_view_name(self):
        return "Lista de Empleados"


class EmpleadoRetrieveAPIView(RetrieveAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

    def get_view_name(self):
        return "Detalle de Empleado"
    
    
# Calendario
def eventos_reservas(request):
    eventos = []
    for reserva in ReservaServicio.objects.all():
        eventos.append({
            "id": reserva.pk,
            "title": f"{reserva.servicio_solicitado.nombre} - {reserva.cliente.nombre}",
            "start": reserva.fecha_solicitada_reserva.isoformat(),
        })
    return JsonResponse(eventos, safe=False)
