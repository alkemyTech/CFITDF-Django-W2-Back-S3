from django import forms
from .models import ReservaServicio, Cliente, Servicio, Empleado, Coordinador

class ReservaServicioForm(forms.ModelForm):
    class Meta:
        model = ReservaServicio
        fields = '__all__'
        widgets = {
            'fecha_solicitada_reserva': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
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
