from django.db import models

# Create your models here.

class Articulo( models.Model ):
    articulo_id = models.AutoField(primary_key=True)
    titulo = models.CharField(1000)
    precio = models.CharField(1000)
    descripcion = models.CharField(1000)
    
    class Meta:
        app_label = 'app_scrapy'
        

    def __str__(self) -> str:
        return str(self.titulo)
