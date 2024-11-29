# Generated by Django 4.2.7 on 2023-11-25 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(max_length=250)),
                ('fecha_emitida', models.DateTimeField(auto_now=True)),
                ('cantidad', models.DecimalField(decimal_places=0, default=0, max_digits=2)),
                ('descuentos', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('importe_gravado', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('importe_exonerado', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('ISV_15', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('ISV_18', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('sub_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('total_pagar', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('descuento', models.DecimalField(decimal_places=0, default=0, max_digits=2)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturas.factura')),
            ],
        ),
    ]