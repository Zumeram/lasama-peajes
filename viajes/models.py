from django.db import models
class Viaje(models.Model):
    codigo=models.CharField(max_length=100,unique=True)
    origen=models.CharField(max_length=100,default='Rengo')
    destino=models.CharField(max_length=100,default='Chiloé')
    fecha_inicio=models.DateTimeField(auto_now_add=True)
    finalizado=models.BooleanField(default=False)
    def __str__(self): return self.codigo
class Peaje(models.Model):
    viaje=models.ForeignKey(Viaje,on_delete=models.CASCADE,related_name='peajes')
    tipo=models.CharField(max_length=20,default='TRONCAL')
    nombre=models.CharField(max_length=200)
    monto=models.IntegerField()
    fecha=models.DateTimeField(auto_now_add=True)
    imagen=models.ImageField(upload_to='boletas/',null=True,blank=True)
