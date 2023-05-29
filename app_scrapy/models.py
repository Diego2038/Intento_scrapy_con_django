from django.db import models

# Create your models here.

class Articulo( models.Model ):
    articulo_id = models.AutoField(primary_key=True)
    titulo = models.CharField(1000)
    precio = models.CharField(1000)
    descripcion = models.CharField(1000)
