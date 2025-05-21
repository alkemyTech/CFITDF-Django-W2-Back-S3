from django.urls import path
from . import views

app_name = 'WebApp'

urlpatterns = [
    #path('', views.home, name='home'),

    # Empleado
    path('empleado/crear/', views.EmpleadoCreateView.as_view(), name='empleado_crear'),
    path('empleado/<int:pk>/', views.EmpleadoDetailView.as_view(), name='empleado_detalle'),
    #path('empleado/', views.EmpleadoListView.as_view(), name='empleado_listar'),
    path('empleado/listar/', views.EmpleadoListView.as_view(), name='empleado_listar'),
    #path('empleado/listar/inactivos/', views.EmpleadoListView.as_view(), {'inactivos': True}, name='empleado_listar_inactivos'),
    path('empleado/listar/inactivos/', views.EmpleadoListView.as_view(), name='empleado_listar_inactivos'),
    path('empleado/editar/<int:pk>/', views.EmpleadoUpdateView.as_view(), name='empleado_editar'),
    path('empleado/cambiar_estado/<int:pk>/', views.empleado_cambiar_estado, name='empleado_cambiar_estado'),
]