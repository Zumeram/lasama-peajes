from django.contrib import admin
from .models import Viaje,Peaje
@admin.register(Viaje)
class ViajeAdmin(admin.ModelAdmin):
    list_display=('codigo','origen','destino','finalizado','fecha_inicio')
@admin.register(Peaje)
class PeajeAdmin(admin.ModelAdmin):
    list_display=('viaje','tipo','nombre','monto')
