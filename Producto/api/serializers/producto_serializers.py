from rest_framework import serializers

from Producto.models import Producto
from ..serializers.valoresProducto_serializer import ValoresProductoCreateSerializer
from Producto.models import ValoresProducto
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'usuario',"fotografia"]


class ProductoCreateSerializer(serializers.ModelSerializer):
    valores = ValoresProductoCreateSerializer(many=True, write_only=True)
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'usuario','valores','fotografia']


    def create(self, validated_data):
        # Extraer los datos de los valores
        valores_data = validated_data.pop('valores')
        # Crear el producto
        producto = Producto.objects.create(**validated_data)
        # Crear los valores asociados
        for valor_data in valores_data:
            ValoresProducto.objects.create(producto=producto, **valor_data)
        return producto


class ProductoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion']
