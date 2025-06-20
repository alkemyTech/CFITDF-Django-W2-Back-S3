from django.urls import path
from . import views

app_name = 'WebApp'

urlpatterns = [
    path('', views.calendario, name='calendario'),
    path('home/', views.home, name='home'),
    # Servicios
    path('servicios/crear/', views.ServicioCreateView.as_view(), name='servicio_crear'),
    path('servicios/<int:pk>/', views.ServicioDetailView.as_view(), name='servicio_detalle'),
    path('servicios/', views.ServicioListView.as_view(), name='servicio_listar'),
    path('servicios/listar/', views.ServicioListView.as_view(), name='servicio_listar'),
    path('servicios/listar/inactivos/', views.ServicioListView.as_view(), {'inactivos': True}, name='servicio_listar_inactivos'),
    path('servicios/editar/<int:pk>/', views.ServicioUpdateView.as_view(), name='servicio_editar'),
    path('servicios/cambiar_estado/<int:pk>/', views.servicio_cambiar_estado, name='servicio_cambiar_estado'),
    # Empleado
    path('empleado/crear/', views.EmpleadoCreateView.as_view(), name='empleado_crear'),
    path('empleado/<int:pk>/', views.EmpleadoDetailView.as_view(), name='empleado_detalle'),
    path('empleado/', views.EmpleadoListView.as_view(), name='empleado_listar'),
    path('empleado/listar/', views.EmpleadoListView.as_view(), name='empleado_listar'),
    path('empleado/listar/inactivos/', views.EmpleadoListView.as_view(), {'inactivos': True}, name='empleado_listar_inactivos'),
    path('empleado/editar/<int:pk>/', views.EmpleadoUpdateView.as_view(), name='empleado_editar'),
    path('empleado/cambiar_estado/<int:pk>/', views.empleado_cambiar_estado, name='empleado_cambiar_estado'),
    # Cliente
    path('cliente/crear/', views.ClienteCreateView.as_view(), name='cliente_crear'),
    path('cliente/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente_detalle'),
    path('cliente/', views.ClienteListView.as_view(), name='cliente_listar'),
    path('cliente/listar/', views.ClienteListView.as_view(), name='cliente_listar'),
    path('cliente/listar/inactivos/', views.ClienteListView.as_view(), {'inactivos':True}, name='cliente_listar_inactivos'),
    path('cliente/editar/<int:pk>/', views.ClienteUpdateView.as_view(), name='cliente_editar'),
    path('cliente/cambiar_estado/<int:pk>/', views.cliente_cambiar_estado, name='cliente_cambiar_estado'),
     #Coordinador
    path('coordinador/crear/', views.CoordinadorCreateView.as_view(), name='coordinador_crear'),
    path('coordinador/<int:pk>/', views.CoordinadorDetailView.as_view(), name = 'coordinador_detalle'),
    path('coordinador/', views.CoordinadorListView.as_view(), name = 'coordinador_listar'),
    path('coordinador/listar/', views.CoordinadorListView.as_view(), name = 'coordinador_listar'),
    path('coordinador/listar/inactivos/', views.CoordinadorListView.as_view(), {'inactivos':True}, name = 'coordinador_listar_inactivos'),
    path('coordinador/editar/<int:pk>/', views.CoordinadorUpdateView.as_view(), name='coordinador_editar'),
    path('coordinador/cambiar_estado/<int:pk>/', views.coordinador_cambiar_estado, name='coordinador_cambiar_estado'),
    # ReservaServicio
    path('reserva_servicio/crear/', views.ReservaServicioCreateView.as_view(), name='reserva_servicio_crear'),
    path('reserva_servicio/<int:pk>/', views.ReservaServicioDetailView.as_view(), name='reserva_servicio_detalle'),
    path('reserva_servicio/', views.ReservaServicioListView.as_view(), name='reserva_servicio_listar'),
    path('reserva_servicio/listar/', views.ReservaServicioListView.as_view(), name='reserva_servicio_listar'),
    path("reserva_servicio/borrar/<int:pk>", views.ReservaServicioDeleteView.as_view(), name="reserva_servicio_borrar"),
    path('reserva_servicio/editar/<int:pk>/', views.ReservaServicioUpdateView.as_view(), name='reserva_servicio_editar'),
    # Calendario
    path('calendario/', views.calendario, name='calendario'),
]