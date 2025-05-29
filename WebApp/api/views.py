#from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ServicioSerializer
from servicios.models import Servicio

# Create your views here.
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