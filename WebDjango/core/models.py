from django.db import models


# Create your models here.


#Modelo para el Usuario
opciones_regiones=[
    [15,"Arica y Parinacota"],
    [1,"Tarapacá"],
    [2,"Antofagasta"],
    [3,"Atacama"],
    [4,"Coquimbo"],
    [5,"Valparaíso"],
    [13,"Metropolitana de Santiago"],
    [6,"Del libertador Gral. Bernardo O'Higgins"],
    [7,"Del Maule"],
    [8,"Del BioBío"],
    [9,"De la Araucanía"],
    [14,"De los Ríos"],
    [10,"De los Lagos"],
    [11,"Aysén del Gral. Carlos Ibáñez del Campo"],
    [12,"Magallanes y de la Antártica Chilena"],
    [16,"Ñuble"],
]
class Usuario(models.Model):
    usuario = models.CharField(max_length=16, primary_key=True, verbose_name='Nombre de Usuario')
    nombre = models.CharField(max_length=40, verbose_name='Nombre Persona')
    password = models.CharField(max_length=30,verbose_name='Password')
    repcontraseña = models.CharField(verbose_name='Repetir contraseña', max_length=100, default='')
    correo = models.EmailField(max_length=100,verbose_name='Correo electronico')
    telefono = models.IntegerField(verbose_name='Telefono')

    def __str__(self):
        return self.usuario


#Modelo para el Envio

class Envio(models.Model):    
    rut = models.CharField(primary_key=True,max_length=10, verbose_name='Rut Persona')
    nombre = models.CharField(max_length=40, verbose_name='Nombre Persona')
    email = models.EmailField(max_length=100, verbose_name='Correo Electronico')
    phone = models.IntegerField(verbose_name='Numero Celular')
    region = models.IntegerField(verbose_name='Region', max_length=100, null=True, blank=True, choices=opciones_regiones)
    comuna = models.CharField(verbose_name='Comuna', max_length=100, null=True, blank=True)
    calle = models.CharField(max_length=100,verbose_name='Calle')
    casa = models.CharField(max_length=5,verbose_name='Numero Casa/Depto')

    def __str__(self):
        return self.rut