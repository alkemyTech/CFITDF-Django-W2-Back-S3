from django import forms
from .models import ReservaServicio, Cliente, Servicio, Empleado, Coordinador

class ReservaServicioForm(forms.ModelForm):
    class Meta:
        model = ReservaServicio
        fields = '__all__'
        widgets = {
            'fecha_solicitada': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].queryset = Cliente.objects.filter(activo=True)
        self.fields['servicio'].queryset = Servicio.objects.filter(activo=True)
        self.fields['empleado'].queryset = Empleado.objects.filter(activo=True)
        self.fields['coordinador'].queryset = Coordinador.objects.filter(activo=True)
