# Generated by Django 4.2.7 on 2023-11-27 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0011_detallefactura'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='productos',
        ),
        migrations.DeleteModel(
            name='DetalleFactura',
        ),
        migrations.AddField(
            model_name='factura',
            name='productos',
            field=models.TextField(default=''),
        ),
    ]
