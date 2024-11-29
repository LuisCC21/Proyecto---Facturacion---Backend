from django.db import models
from jsonfield import JSONField

# Create your models here.




class Producto(models.Model):
    name = models.CharField(max_length=100)
    descuento = models.DecimalField(max_digits=4, decimal_places=2, default=00.00)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0, null=False)
    img = models.TextField(default='')
    cantidad_disponible = models.IntegerField(default=0)


class Factura(models.Model):
    nombre_cliente = models.CharField(max_length=250)
    num_factura = models.CharField(max_length=50,default='')
    RTN_cliente = models.CharField(max_length=50,default='')
    RTN_empresa = models.CharField(max_length=50, default='0801-900-3249605')
    fecha_emitida = models.DateTimeField(auto_now=True)
    productos =  models.CharField(max_length=1000)
    descuentos = models.DecimalField(max_digits=4, decimal_places=2, default=0.0, null=False)
    importe_gravado = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    importe_exonerado = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    ISV_15 = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    ISV_18 = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    sub_total =  models.DecimalField(max_digits=8, decimal_places=2, default=0.0, null=False)
    total_pagar =  models.DecimalField(max_digits=8, decimal_places=2, default=0.0, null=False)

