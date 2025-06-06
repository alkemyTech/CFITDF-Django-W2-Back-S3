from django.urls import path
from .views import (
    ServicioListAPIView, ServicioRetrieveAPIView, 
    ClienteListApiView, ClienteRetrieveAPIView,
    CoordinadorAPIView, CoordinadorRetriveAPIView,
    EmpleadoListAPIView, EmpleadoRetrieveAPIView,
    eventos_reservas
)

app_name = 'api'

urlpatterns = [
    # Servicios
    path('servicios/', ServicioListAPIView.as_view(), name='servicio_listar'),
    path('servicios/<int:pk>/', ServicioRetrieveAPIView.as_view(), name='servicio_detalle'),
    # Clientes
    path('clientes/', ClienteListApiView.as_view(), name='cliente_listar'),
    path('clientes/<int:pk>/', ClienteRetrieveAPIView.as_view(), name='cliente_detalle'),
    # Coordinadores
    path('coordinadores/', CoordinadorAPIView.as_view(), name='coordinador_listar'),
    path('coordinadores/<int:pk>/', CoordinadorRetriveAPIView.as_view(), name='coordinador_detalle'),
    # Empleados
    path('empleados/', EmpleadoListAPIView.as_view(), name='empleado_listar'),
    path('empleados/<int:pk>/', EmpleadoRetrieveAPIView.as_view(), name='empleado_detalle'),
    # Calendario
    path('eventos/', eventos_reservas, name='eventos_reservas'),
]
