# Generated by Django 4.2.7 on 2023-11-27 08:11

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0012_remove_factura_productos_delete_detallefactura_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='productos',
            field=jsonfield.fields.JSONField(default=list),
        ),
    ]
