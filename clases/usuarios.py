from clases.producto import Producto
from clases.carrito import Carrito
import os

class Usuario:
    def __init__(self,nombre):
        self.nombre = nombre

    def menu(self):
        pass

class Admin(Usuario):
    def menu(self,catalogo):
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            print("--- Menú Admin ---")
            print("1- Listar catálogo")
            print("2- Crear producto en catálogo")
            print("3- Eliminar producto en catálogo")
            print("4- Guardar en archivo")

            opcion = input("Ingrese su opción: ")

            if opcion == "1":
                catalogo.listar_catalogo()
            elif opcion =="2":
                id = int(input("id de producto"))
                nombre = input("nombre del producto")
                categoria = input("categoria del producto")
                precio = int(input("precio del producto"))
                catalogo.agregar_producto(Producto(id,nombre,categoria,precio))
            elif opcion =="3":
                id = int(input("id a borrar"))
                catalogo.eliminar_producto(id)
            elif opcion =="4":
                catalogo.guardar_catalogo()
            else:
                print("pon una opcion valida")
        
class Cliente(Usuario):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.carrito = Carrito()

    def menu(self,catalogo):
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            print("menu cliente")
            print("1- ver catalogo")
            print("2- agregar al carrito")
            print("3- ver carrito")
            print("4- comprar")

            opcion = input("ingrese su opcion: ")

            if opcion == "1":
                catalogo.listar_catalogo()
            elif opcion =="2":
                id = int(input("ingrese el id del producto"))
                cantidad = int(input("cantidad"))
                producto= catalogo.buscar_por_id(id)
                self.carrito.agregar(producto,cantidad)

            elif opcion =="3":
                self.carrito.ver_carrito()
            elif opcion =="4":
                self.carrito.pagar()
                self.carrito.vaciar()
            else:
                print("opcion no valida!!!")
                
            




