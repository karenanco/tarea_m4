from clases.catalogo import Catalogo
from clases.usuarios import Admin, Cliente
from clases.producto import Producto
from clases.carrito import Carrito
import os

class Tienda:
    def __init__(self):
        self.catalogo = Catalogo()
        self.cargar_datos()

    def cargar_datos(self):
        self.catalogo.agregar_producto(Producto(1,"Té rojo con bergamota","Blends",3290))
        self.catalogo.agregar_producto(Producto(2,"Té verde con frutos rojos","Blends",3399))
        self.catalogo.agregar_producto(Producto(3,"Té blanco con manzanilla ","Blends",3490))
        self.catalogo.agregar_producto(Producto(4,"Té verde con menta y limón","Blends",3590))
        self.catalogo.agregar_producto(Producto(5,"Té verde con rosa y lavanda","Blends",3690))
        self.catalogo.agregar_producto(Producto(6,"Té rooibos con manzanilla y cedrón","Blends",4290))
        self.catalogo.agregar_producto(Producto(7,"Té rooibos con coco y chocolate","Blends",4499))
        self.catalogo.agregar_producto(Producto(8,"Té negro con vainilla y naranja","Blends",4699))

    def iniciar(self):
        print("1- Admin")
        print("2- Cliente")

        opcion = input("Seleccione el rol: ")

        if opcion == "1":
            admin = Admin("Admin")
            admin.menu(self.catalogo)

        elif opcion =="2":
            cliente = Cliente("Cliente")
            cliente.menu(self.catalogo)


if __name__ == "__main__":
    tienda = Tienda()
    tienda.iniciar()



