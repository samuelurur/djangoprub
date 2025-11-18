from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction
from django.contrib import messages
from .models import Product, Pedido, PedidoItem


# Página principal de la tienda
def tienda(request):
    productos = Product.objects.all()
    return render(request, 'tienda/tienda.html', {'productos': productos})


# Agregar producto al carrito
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Product, id=producto_id)
    carrito = request.session.get('carrito', {})

    if str(producto.id) in carrito:
        carrito[str(producto.id)]['cantidad'] += 1
    else:
        carrito[str(producto.id)] = {
            'nombre': producto.name,
            'precio': float(producto.price),
            'cantidad': 1,
            'imagen': producto.imagen.url if producto.imagen else ''
        }

    request.session['carrito'] = carrito
    request.session.modified = True
    return redirect('Tienda:tienda')


# Ver carrito
def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    total = 0

    for item in carrito.values():
        item['subtotal'] = item['precio'] * item['cantidad']
        total += item['subtotal']

    return render(request, 'tienda/carrito.html', {
        'carrito': carrito,
        'total': total
    })


# Aumentar cantidad
def aumentar_cantidad(request, producto_id):
    carrito = request.session.get('carrito', {})
    producto_id = str(producto_id)
    if producto_id in carrito:
        carrito[producto_id]['cantidad'] += 1
        request.session['carrito'] = carrito
        request.session.modified = True
    return redirect('Tienda:ver_carrito')


# Disminuir cantidad
def disminuir_cantidad(request, producto_id):
    carrito = request.session.get('carrito', {})
    producto_id = str(producto_id)
    if producto_id in carrito:
        carrito[producto_id]['cantidad'] -= 1
        if carrito[producto_id]['cantidad'] <= 0:
            del carrito[producto_id]
        request.session['carrito'] = carrito
        request.session.modified = True
    return redirect('Tienda:ver_carrito')


# Eliminar producto
def eliminar_del_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    producto_id = str(producto_id)
    if producto_id in carrito:
        del carrito[producto_id]
        request.session['carrito'] = carrito
        request.session.modified = True
    return redirect('Tienda:ver_carrito')


# Vaciar carrito
def vaciar_carrito(request):
    request.session['carrito'] = {}
    request.session.modified = True
    return redirect('Tienda:ver_carrito')


# Finalizar compra
@transaction.atomic
def finalizar_compra(request):
    if request.method != 'POST':
        return redirect('Tienda:ver_carrito')

    carrito = request.session.get('carrito', {})

    if not carrito:
        messages.warning(request, "Tu carrito está vacío.")
        return redirect('Tienda:ver_carrito')

    total = sum(item['precio'] * item['cantidad'] for item in carrito.values())
    pedido = Pedido.objects.create(total=total)

    for item in carrito.values():
        producto = Product.objects.get(name=item['nombre'])
        PedidoItem.objects.create(
            pedido=pedido,
            producto=producto,
            cantidad=item['cantidad'],
            precio_unitario=item['precio']
        )

        producto.stock = max(0, producto.stock - item['cantidad'])
        producto.save()

    request.session['carrito'] = {}
    request.session.modified = True

    messages.success(request, f"Compra finalizada correctamente. Pedido #{pedido.id} registrado.")
    return redirect('Tienda:tienda')
