from producto import Producto


class Catalogo:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self,producto):
        self.productos.append(producto)

    def listar_catalogo(self):
        for producto in self.productos:
            print(producto)

    def eliminar_producto(self,id):
        pass
