from django.urls import path
from .views import(
    CoordinadorAPIView
)

app_name = 'api'

urlpatterns = [
    path('api-coordinador', CoordinadorAPIView.as_view(), name='api-coordinador')
]
