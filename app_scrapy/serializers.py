from rest_framework import serializers
from .models import Articulo

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'
        
    def create(self, validated_data):
        return Articulo.objects.create(**validated_data)