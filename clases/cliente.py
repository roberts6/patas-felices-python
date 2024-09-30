class Cliente:
    contador_id = 1  # Variable de clase que mantiene el siguiente ID disponible
    
    def __init__(self, nombre, direccion, telefono):
        self.id = Cliente.generar_id()  # Llamada al método de clase para generar el ID único
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.historial_compras_cliente = []

    @classmethod
    def generar_id(cls):
        """Genera un ID único para cada cliente."""
        id_actual = cls.contador_id
        cls.contador_id += 1
        return id_actual
    
    def actualizar_informacion(self, direccion=None, telefono=None):
        if direccion:
            self.direccion = direccion
        if telefono:
            self.telefono = telefono
            
    def registrar_compra(self, compra):
        self.historial_compras_cliente.append(compra)
        
    def mostrar_informacion(self):
        return f'''El cliente es {self.nombre}
                   Dirección: {self.direccion}
                   Teléfono: {self.telefono}'''