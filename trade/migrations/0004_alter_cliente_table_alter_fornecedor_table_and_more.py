# Generated by Django 5.0.7 on 2024-07-19 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0003_alter_cliente_table_alter_fornecedor_table_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cliente',
            table='cliente',
        ),
        migrations.AlterModelTable(
            name='fornecedor',
            table='fornecedor',
        ),
        migrations.AlterModelTable(
            name='itensvenda',
            table='itensvenda',
        ),
        migrations.AlterModelTable(
            name='produto',
            table='produto',
        ),
        migrations.AlterModelTable(
            name='venda',
            table='venda',
        ),
        migrations.AlterModelTable(
            name='vendedor',
            table='vendedor',
        ),
    ]
