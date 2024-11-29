from rest_framework import serializers
from .models import Factura, Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
       
class FacturaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Factura
        fields = '__all__' 
        read_only_fields = ('fecha_emitida',)

        
