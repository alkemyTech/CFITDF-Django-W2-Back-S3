from django.urls import path
from .views import ServicioListAPIView, ServicioRetrieveAPIView, CoordinadorAPIView

app_name = 'api'

urlpatterns = [
    # Servicios
    path('servicios/', ServicioListAPIView.as_view(), name='servicio_listar'),
    path('servicios/<int:pk>/', ServicioRetrieveAPIView.as_view(), name='servicio_detalle'),
    # Coordinadores
    path('coordinadores/', CoordinadorAPIView.as_view(), name='coordinador_listar'),
]