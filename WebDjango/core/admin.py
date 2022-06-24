from django.contrib import admin
from .models import Usuario, Envio
# Register your models here.

#Administrar el modelo completo

admin.site.register(Usuario)
admin.site.register(Envio)