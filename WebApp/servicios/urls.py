from django.urls import path
from . import views

app_name = 'WebApp'

urlpatterns = [
    #path('', views.home, name='home'),

    # Servicios
    path('servicios/crear/', views.ServicioCreateView.as_view(), name='servicio_crear'),
    #Coordinador
    path('coordinador/crear/', views.CoordinadorCreateView.as_view(), name='coordinador_crear')

]