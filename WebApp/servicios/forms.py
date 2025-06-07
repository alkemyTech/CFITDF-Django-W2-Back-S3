from django import forms
from .models import ReservaServicio, Cliente, Servicio, Empleado, Coordinador
from django.forms import DateTimeInput

class ReservaServicioForm(forms.ModelForm):
    class Meta:
        model = ReservaServicio
        fields = '__all__'
        widgets = {
            'fecha_solicitada_reserva': DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'cliente' in self.fields:
            self.fields['cliente'].queryset = Cliente.objects.filter(activo=True)
        if 'servicio_solicitado' in self.fields:
            self.fields['servicio_solicitado'].queryset = Servicio.objects.filter(activo=True)
        if 'empleado_encargado' in self.fields:
            self.fields['empleado_encargado'].queryset = Empleado.objects.filter(activo=True)
        if 'coordinador_asignado' in self.fields:
            self.fields['coordinador_asignado'].queryset = Coordinador.objects.filter(activo=True)
        if self.instance and self.instance.pk:
            self.fields['fecha_solicitada_reserva'].initial = self.instance.fecha_solicitada_reserva.strftime('%Y-%m-%dT%H:%M')

class CoordinadorForm(forms.ModelForm):
    class Meta:
        model = Coordinador
        fields = '__all__'
        widgets = {
            'fecha_alta': DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
        }