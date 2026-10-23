from django.db import models

class Viaje(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    origen = models.CharField(max_length=100, blank=True, default="")
    destino = models.CharField(max_length=100, blank=True, default="")
    patente = models.CharField(max_length=20, blank=True, default="")
    chofer = models.CharField(max_length=100, blank=True, default="")
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    finalizado = models.BooleanField(default=False)

    def __str__(self):
        return self.codigo

class Peaje(models.Model):
    viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE, related_name="peajes")
    tipo = models.CharField(max_length=20, choices=[('troncal','Troncal'),('barcaza','Barcaza')], default="troncal")
    monto = models.IntegerField(default=0)
    nombre_peaje = models.CharField(max_length=100, blank=True, default="")
    foto = models.ImageField(upload_to="boletas/", blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.viaje.codigo} - ${self.monto}"
