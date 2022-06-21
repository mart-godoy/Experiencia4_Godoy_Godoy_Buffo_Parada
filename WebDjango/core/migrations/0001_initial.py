# Generated by Django 4.0.4 on 2022-06-06 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Rut Persona')),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre Persona')),
                ('email', models.EmailField(max_length=100, verbose_name='Correo Electronico')),
                ('phone', models.IntegerField(verbose_name='Numero Celular')),
                ('ciudad', models.CharField(max_length=50, verbose_name='Ciudad')),
                ('comuna', models.CharField(max_length=50, verbose_name='Comuna')),
                ('calle', models.CharField(max_length=100, verbose_name='Calle')),
                ('casa', models.CharField(max_length=5, verbose_name='Numero Casa/Depto')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('usuario', models.CharField(max_length=16, primary_key=True, serialize=False, verbose_name='Nombre de Usuario')),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre Persona')),
                ('password', models.CharField(max_length=30, verbose_name='Password')),
                ('correo', models.EmailField(max_length=100, verbose_name='Correo electronico')),
                ('telefono', models.IntegerField(verbose_name='Telefono')),
            ],
        ),
    ]