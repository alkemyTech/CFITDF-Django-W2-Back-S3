#from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ServicioSerializer, CoordinadorSerializer, EmpleadoSerializer
from servicios.models import Servicio, Coordinador, Empleado

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
    
    
# Coordinadores
class CoordinadorAPIView(ListAPIView):
    queryset = Coordinador.objects.all()
    serializer_class = CoordinadorSerializer


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