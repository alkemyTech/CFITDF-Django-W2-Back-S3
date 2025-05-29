from rest_framework.serializers import ModelSerializer
from servicios.models import Servicio, Cliente, Empleado, Coordinador

class ServicioSerializer(ModelSerializer):
    class Meta:
        model = Servicio
        fields = ['pk', 'nombre', 'descripcion', 'precio','activo']
        

class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = ["pk", "nombre", "apellido", "activo"]


class EmpleadoSerializer(ModelSerializer):
    class Meta:
        model = Empleado
        fields = ["pk", "nombre", "apellido", "numero_legajo", "activo"]
        

class CoordinadorSerializer(ModelSerializer):
    class Meta:
        model = Coordinador
        fields = ["pk", "nombre", "apellido", "numero_documento", "fecha_alta", "activo"]           