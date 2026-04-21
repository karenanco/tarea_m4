from datetime import datetime

class ErrorCarritoVacio(Exception):
    pass

class Carrito:
    def __init__(self):
        self.items = {}

    def __str__(self):
        return f"{self.items}"

    def agregar(self,producto,cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0")
            return
        
        if cantidad >= 1:
            print("Producto(s) agregado(s) exitosamente")

        if producto in self.items:
            self.items[producto] += cantidad
        else:
            self.items[producto] = cantidad

    def ver_carrito(self):
        total = 0
        if len(self.items) == 0:
            print("El carrito está vacío. Agrégale productos.")
            return 0
        
        for p,c in self.items.items():
            subtotal = p.precio * c
            total += subtotal
            print(f"{p.nombre} - Cantidad: {c}- Subtotal: ${subtotal}")
        print(f"Total de la compra: ${total}")
        return total
    
    def vaciar(self):
        self.items.clear()

    def confirmar_compra(self):
        try:
            if not self.items:
                raise ErrorCarritoVacio("No se puede confirmar la compra porque el carrito está vacío.")

            total = 0
            ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open("ordenes.txt", "a", encoding="utf-8") as f:
                f.write(f"--- Orden de Compra: {ahora} ---")
                for p, c in self.items.items():
                    subtotal = p.precio * c
                    total += subtotal
                    f.write(f"Producto: {p.nombre} | Cantidad: {c} | Subtotal: ${subtotal}")
                f.write(f"TOTAL PAGADO: ${total}")
                f.write("-" * 40 + "\n\n")

            self.vaciar()
            print("Compra confirmada")

        except ErrorCarritoVacio as e:
            print(f"Error: {e}")
       
    





