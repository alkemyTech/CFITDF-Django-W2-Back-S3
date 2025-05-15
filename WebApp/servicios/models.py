from django.db import models

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.IntegerField()
    activo = models.BooleanField(default=True)


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)


class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numero_legajo = models.IntegerField()
    activo = models.BooleanField(default=True)

class Coordinador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    numero_documento = models.IntegerField()
    fecha_alta = models.DateField()
    activo = models.BooleanField(default=True)

    class Meta():
        verbose_name_plural = 'Coordinadores'


class ReservaServicio(models.Model):
    fecha_registro_reserva = models.DateTimeField(auto_now_add=True)
    fecha_indicada_reserva = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    coordinador = models.ForeignKey(Coordinador, on_delete=models.CASCADE)
    
    def __str__(self):
        return F"{self.fecha_indicada_reserva}, {self.fecha_registro_reserva}"

    class Meta():
        ordering = ['fecha_indicada_reserva']