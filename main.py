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
        self.catalogo.agregar_producto(Producto(1,"telefono","tecnologia",1000))
        self.catalogo.agregar_producto(Producto(2,"telefono","tecnologia",1000))
        self.catalogo.agregar_producto(Producto(3,"telefono","tecnologia",1000))
        self.catalogo.agregar_producto(Producto(4,"telefono","tecnologia",1000))
        self.catalogo.agregar_producto(Producto(5,"telefono","tecnologia",1000))
        self.catalogo.agregar_producto(Producto(6,"telefono","tecnologia",1000))
        self.catalogo.agregar_producto(Producto(7,"telefono","tecnologia",1000))
        self.catalogo.agregar_producto(Producto(8,"telefono","tecnologia",1000))

    def iniciar(self):
        print("1- admin")
        print("2- cliente")

        opcion = input("seleccione el rol")

        if opcion == "1":
            admin = Admin("admin")
            admin.menu(self.catalogo)

        elif opcion =="2":
            cliente = Cliente("cliente")
            cliente.menu(self.catalogo)


if __name__ == "__main__":
    tienda = Tienda()
    tienda.iniciar()



