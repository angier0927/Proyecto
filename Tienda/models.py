from django.db import models

# Create your models here.

class Articulo(models.Model):
    id = models.AutoField(primary_key = True)
    nombre_producto = models.CharField(max_length = 60)
    precio = models.IntegerField(blank=True, null=True)
    categoria = models.CharField(max_length=50)
    disponibilidad = models.CharField(max_length= 10)
    descuento = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nombre_producto



