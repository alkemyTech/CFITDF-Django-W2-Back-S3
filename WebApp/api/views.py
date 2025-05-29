#from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ServicioSerializer, CoordinadorSerializer
from servicios.models import Servicio, Coordinador

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
