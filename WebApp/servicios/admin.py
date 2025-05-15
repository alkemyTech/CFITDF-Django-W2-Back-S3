from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'precio', 'activo']
    search_fields = ['nombre']


@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'activo']
    search_fields = ['nombre', 'apellido']


@admin.register(models.Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'activo']
    search_fields = ['nombre', 'apellido']
