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
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numero_documento = models.IntegerField()
    fecha_alta = models.DateTimeField()
    activo = models.BooleanField(default=True)


class ReservaServicio(models.Model):
    fecha_registro_reserva = models.DateTimeField()
    fecha_solicitada_reserva = models.DateTimeField()
    servicio_solicitado = models.ForeignKey(Servicio, on_delete=models.CASCADE, related_name="servicio")
    empleado_encargado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="empleado")
    coordinador_asignado = models.ForeignKey(Coordinador, on_delete=models.CASCADE, related_name="coordinador")