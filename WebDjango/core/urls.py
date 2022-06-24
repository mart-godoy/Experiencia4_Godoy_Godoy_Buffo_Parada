from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('index',views.index),
    path('formsuge',views.formsuge),
    path('compra',views.compra),
    path('nosotros',views.nosotros),
    path('venta',views.venta),
    path('creacionuser',views.creacionuser),
    path('leer',views.leer),
    path('modUsuario/<usuario>',views.modUsuario),
    path('modifUsuario/',views.modifUsuario),
    path('ventleer',views.ventleer),
    path('registrarUsuario/',views.registrarUsuario),
    path('registrarEnvio/',views.registrarEnvio),
    path('modEnvio/<rut>',views.modEnvio),
    path('modifEnvio/',views.modifEnvio),
    path('segui',views.segui),
    path('app',views.app),



]

# path('',views.),