# Generated by Django 4.2.7 on 2023-11-27 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0007_rename_url_producto_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='cantidad',
        ),
    ]