
class Carrito:
    def __init__(self):
        self.items = {}

    def __str__(self):
        return f"{self.items}"

    def agregar(self,producto,cantidad):
        if producto in self.items:
            self.items[producto] += cantidad
        else:
            self.items[producto] = cantidad

    def ver_carrito(self):
        total = 0
        for p,c in self.items.items():
            subtotal = p.precio * c
            total += subtotal
            print(f"{p.nombre} - Cantidad: {c}- Subtotal: {subtotal}")
        print(f"Total de la compra: {total}")

    def vaciar(self):
        self.items.clear()

    def pagar(self):
        return f"Ingrese el pago"




