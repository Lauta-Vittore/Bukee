# Generated by Django 4.0.6 on 2022-09-09 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_alter_producto_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tallas',
        ),
    ]