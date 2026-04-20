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
                id = int(input("ID de producto: "))
                nombre = input("Nombre del producto: ")
                categoria = input("Categoría del producto: ")
                precio = int(input("Precio del producto: "))
                catalogo.agregar_producto(Producto(id,nombre,categoria,precio))
            elif opcion =="3":
                id = int(input("ID a borrar: "))
                catalogo.eliminar_producto(id)
                print("Producto borrado exitosamente")
            elif opcion =="4":
                catalogo.guardar_catalogo()
                print("Producto guardado exitosamente en el archivo catálogo.txt")
            else:
                print("Marca una opción válida")
        
class Cliente(Usuario):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.carrito = Carrito()

    def menu(self,catalogo):
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            print("--- Menú Cliente ---")
            print("1- Ver catálogo de productos")
            print("2- Agregar productos al carrito")
            print("3- Ver carrito")
            print("4- Comprar productos seleccionados")

            opcion = input("Ingrese su opción: ")

            if opcion == "1":
                catalogo.listar_catalogo()
            elif opcion =="2":
                id = int(input("Ingrese el ID del producto: "))
                cantidad = int(input("Cantidad: "))
                producto= catalogo.buscar_por_id(id)
                self.carrito.agregar(producto,cantidad)

            elif opcion =="3":
                self.carrito.ver_carrito()
            elif opcion =="4":
                self.carrito.confirmar_compra()
                self.carrito.vaciar()
            else:
                print("Opción no válida. Marque otra alternativa")
                
            




