# Generated by Django 4.2.7 on 2023-11-27 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='factura',
        ),
        migrations.AddField(
            model_name='factura',
            name='RTN_cliente',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='factura',
            name='RTN_empresa',
            field=models.CharField(default='0801-900-3249605', max_length=50),
        ),
        migrations.AddField(
            model_name='factura',
            name='num_factura',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='producto',
            name='facturas',
            field=models.ManyToManyField(related_name='productos', to='facturas.factura'),
        ),
        migrations.AddField(
            model_name='producto',
            name='url',
            field=models.TextField(default=''),
        ),
    ]