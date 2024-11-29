from .models import Factura, Producto
from rest_framework import viewsets, permissions
from .serializers import FacturaSerializer, ProductoSerializer


class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FacturaSerializer

  

class ProductoViewSet(viewsets.ModelViewSet):
    queryset= Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer
    