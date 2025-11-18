from decimal import Decimal
from .models import Product

class Carrito:
    def __init__(self, request):
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito

    def agregar(self, producto, cantidad=1):
        producto_id = str(producto.id)
        if producto_id not in self.carrito:
            self.carrito[producto_id] = {
                "id": producto.id,
                "name": producto.name,
                "price": str(producto.price),
                "cantidad": cantidad,
                "imagen": producto.imagen.url if producto.imagen else "",
            }
        else:
            self.carrito[producto_id]["cantidad"] += cantidad
        self.guardar()

    def eliminar(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carrito:
            del self.carrito[producto_id]
            self.guardar()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

    def guardar(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def obtener_total(self):
        return sum(
            Decimal(item["price"]) * item["cantidad"]
            for item in self.carrito.values()
        )

    def __iter__(self):
        for item in self.carrito.values():
            item["total_item"] = Decimal(item["price"]) * item["cantidad"]
            yield item
