class Producto:
    def __init__(self, id, nombre, categoria,precio):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def __str__(self):
        return f"ID de compra: {self.id} - {self.nombre} - Categoría: {self.categoria} - Precio ($): {self.precio}"
    
    def __repr__(self):
        return self.nombre
    
    def __eq__(self, otro):
        if not isinstance(otro, Producto):
            return False
        return self.id == otro.id

    def __hash__(self):
        return hash(self.id)
    