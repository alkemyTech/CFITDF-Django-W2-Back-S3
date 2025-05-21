from django.urls import path
from . import views

app_name = 'WebApp'

urlpatterns = [
    #path('', views.home, name='home'),

    # Servicios
    path('servicios/crear/', views.ServicioCreateView.as_view(), name='servicio_crear'),
    path('servicios/<int:pk>/', views.ServicioDetailView.as_view(), name='servicio_detalle'),
    path('servicios/', views.ServicioListView.as_view(), name='servicio_listar'),
    path('servicios/listar/', views.ServicioListView.as_view(), name='servicio_listar'),
    path('servicios/listar/inactivos/', views.ServicioListView.as_view(), {'inactivos': True}, name='servicio_listar_inactivos'),
]