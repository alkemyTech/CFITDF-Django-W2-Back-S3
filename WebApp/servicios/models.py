from django.db import models

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.IntegerField()
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.nombre}"


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"        


class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numero_legajo = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
            return f"{self.nombre} {self.apellido} ({self.numero_legajo})"    
    

class Coordinador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numero_documento = models.IntegerField()
    fecha_alta = models.DateTimeField()
    activo = models.BooleanField(default=True)
    
    def __str__(self):
            return f"{self.nombre} {self.apellido} ({self.numero_documento})"  
    
    class Meta():
        verbose_name_plural = 'Coordinadores'


class ReservaServicio(models.Model):
    fecha_registro_reserva = models.DateTimeField()
    fecha_solicitada_reserva = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="cliente")
    servicio_solicitado = models.ForeignKey(Servicio, on_delete=models.CASCADE, related_name="servicio")
    empleado_encargado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="empleado")
    coordinador_asignado = models.ForeignKey(Coordinador, on_delete=models.CASCADE, related_name="coordinador")
    
    def __str__(self):
            return f"{self.servicio.nombre} ({self.fecha_solicitada})" 