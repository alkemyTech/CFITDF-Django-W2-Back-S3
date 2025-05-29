from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import CoordinadorSerializer
from servicios.models import Coordinador


# Create your views here.
#Coordinadores
class CoordinadorAPIView(ListAPIView):
    queryset = Coordinador.objects.all()
    serializer_class = CoordinadorSerializer