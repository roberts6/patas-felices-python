class Inventario:
    def __init__(self):
        self.lista_productos = []
        self.contador_id = 1  # Contador para asignar ID único a los productos
        
    def generar_id(self):
        """Genera un ID único para cada producto."""
        id_actual = self.contador_id
        self.contador_id += 1
        return id_actual
    
    def agregar_producto(self, nombre, cantidad, precio):
        """Crea y agrega un producto al inventario con un ID único."""
        producto = {
            'id': self.generar_id(),
            'nombre': nombre,
            'cantidad': cantidad,
            'precio': precio
        }
        self.lista_productos.append(producto)
        print(f"Producto {nombre} agregado con ID {producto['id']}")
        
    def mostrar_productos(self):
        """Muestra todos los productos en el inventario."""
        if not self.lista_productos:
            print("El inventario está vacío.")
        else:
            for producto in self.lista_productos:
                print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}")
    
    def actualizar_producto(self, id_producto, nombre=None, cantidad=None, precio=None):
        """Actualiza los detalles de un producto por su ID."""
        for producto in self.lista_productos:
            if producto['id'] == id_producto or producto["nombre"] == nombre:
                if nombre:
                    producto['nombre'] = nombre
                if cantidad:
                    producto['cantidad'] = cantidad
                if precio:
                    producto['precio'] = precio
                print(f"El producto con ID {id_producto} actualizado.")
                return
        print(f"Producto con ID {id_producto} no encontrado.")
    
    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario por su ID."""
        for producto in self.lista_productos:
            if producto['id'] == id_producto:
                self.lista_productos.remove(producto)
                print(f"Producto con ID {id_producto} eliminado.")
                return
        print(f"Producto con ID {id_producto} no encontrado.")
        
    def alerta_stock(self, stock_alerta):
    # Genera una alerta para productos cuyo stock es menor o igual al valor especificado.
        productos_bajo_stock = [producto['nombre'] for producto in self.lista_productos if producto['cantidad'] <= stock_alerta]
    
        if productos_bajo_stock:
            productos_str = ', '.join(productos_bajo_stock)
            return f"Atención: los siguientes productos se están agotando: {productos_str}"
        else:
            return "No hay productos con bajo stock."

        
    def buscar_producto(self, id_producto=None, nombre=None):
        """Busca un producto por ID o nombre y lo devuelve si lo encuentra."""
        for producto in self.lista_productos:
            if (id_producto is not None and producto['id'] == id_producto) or \
               (nombre is not None and producto['nombre'].lower() == nombre.lower()):
                return producto
        print("Producto no encontrado.")
        return None

'''
# Ejemplo de uso
inventario = Inventario()

inventario.agregar_producto("Manzanas", 50, 0.5)
inventario.agregar_producto("Peras", 30, 0.7)
inventario.agregar_producto("Sandia", 30, 1.7)

# Mostrar productos
inventario.mostrar_productos()

producto_encontrado = inventario.buscar_producto(id_producto=2)
if producto_encontrado:
    print(f"Producto encontrado: {producto_encontrado}")


inventario.actualizar_producto(2,cantidad=8)

 
inventario.mostrar_productos()
'''
