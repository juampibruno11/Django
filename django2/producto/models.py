from django.db import models

# Create your models here.
class class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.CharField(max_length=30)
    fecha = models.CharField(max_length=30)
    cantidad = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    
