class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad
        
    def actualizar_cantidad(self, cantidad):
        if cantidad:
            self.cantidad = cantidad
    
    def actualizar_precio(self, precio):
        if precio:
            self.precio = precio
            
    def actualizar_categoria(self, categoria):
        if categoria:
            self.categoria = categoria
            
    def actualizar_nombre(self, nombre):
        if nombre:
            self.nombre = nombre