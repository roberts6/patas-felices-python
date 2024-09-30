from datetime import datetime

# Lista global para almacenar todas las ventas realizadas en la tienda
historial_ventas_global = []

class Venta:
    def __init__(self, cliente, lista_productos, ):
        self.cliente = cliente
        self.lista_productos = lista_productos
        self.fecha = datetime.now()
        self.total = self.calcular_total()

        
    def calcular_total(self):
        return sum(producto['precio'] * producto['cantidad'] for producto in self.lista_productos)
    
    def registrar_venta(self):
        # Agrega la venta al historial del cliente
        self.cliente.registrar_compra(self)
        # Agrega la venta al historial global de ventas de Patas Felices
        historial_ventas_global.append(self)
        return f"Venta registrada: {self.mostrar_informacion()}"
    
    def mostrar_informacion(self):
        productos = ", ".join([producto['nombre'] for producto in self.lista_productos]) 
        return f"Cliente: {self.cliente.nombre}, Productos: {productos}, Total: ${self.total:.2f}, Fecha: {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}"
    
    
    @classmethod #permite accede a la lista 
    def mostrar_ventas_global(cls):
        if not historial_ventas_global:
            return "No hay ventas registradas."
        else:
            # venta.mostrar_informacion() hace referencia a cada instancia de la clase Venta
            ventas_info = [venta.mostrar_informacion() for venta in historial_ventas_global] 
            return "\n".join(ventas_info)