from rest_framework import serializers
from .models import Articulo

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ['articulo_id','titulo','precio','descripcion']
        
    def create(self, validated_data):
        return Articulo.objects.create(**validated_data)