from django.urls import path
from . import views

app_name = 'WebApp'

urlpatterns = [
    #path('', views.home, name='home'),

    # Servicios
    path('servicios/crear/', views.ServicioCreateView.as_view(), name='servicio_crear'),
    #Coordinador
    path('coordinador/crear/', views.CoordinadorCreateView.as_view(), name='coordinador_crear'),
    path('coordinador/<int:pk>/', views.CoordinadorDetailView.as_view(), name = 'coordinador_detalle'),
    path('coordinador/', views.CoordinadorListView.as_view(), name = 'coordinador_listar'),
    path('coordinador/inactivos', views.CoordinadorListView.as_view(), {'inactivos':True}, name = 'coordinador_listar_inactivos'),

]