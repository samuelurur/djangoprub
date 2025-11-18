from django.urls import path
from . import views

app_name = 'Tienda'

urlpatterns = [
    path('', views.tienda, name='tienda'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('vaciar/', views.vaciar_carrito, name='vaciar_carrito'),
    path('aumentar/<int:producto_id>/', views.aumentar_cantidad, name='aumentar_cantidad'),
    path('disminuir/<int:producto_id>/', views.disminuir_cantidad, name='disminuir_cantidad'),
    path('finalizar/', views.finalizar_compra, name='finalizar_compra'),
]
