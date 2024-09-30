# -------------------------------------------

# Funciones

# -------------------------------------------
from clases.mascota import Perro, Gato
from clases.cliente import Cliente
from clases.inventario import Inventario
from clases.venta import Venta


def registrar_mascota():
    """Registra una mascota (Perro o Gato) en el sistema."""
    tipo = input("Por favor ingresá qué tipo de mascota es (perro / gato): ").strip().lower()
    nombre = input("Nombre de la mascota: ").strip()
    try:
        edad = int(input("¿Qué edad tiene? "))
    except ValueError:
        print("La edad debe ser un número entero.")
        return
    
    salud = input("¿Qué es lo que le pasa? ").strip()
    try:
        precio = float(input("Precio de atención: $"))
    except ValueError:
        print("El precio debe ser un número.")
        return
    
    if tipo == "perro":
        raza = input("Ingresa de qué raza es: ").strip()
        try:
            nivel_de_energia = int(input("¿Cuál es su nivel de energía (1 al 10)? "))
            if nivel_de_energia < 1 or nivel_de_energia > 10:
                raise ValueError
        except ValueError:
            print("El nivel de energía debe ser un número entre 1 y 10.")
            return
        mascota = Perro(nombre, edad, salud, precio, raza, nivel_de_energia)
    
    elif tipo == "gato":
        raza = input("Ingresa de qué raza es: ").strip()
        try:
            independencia = int(input("Qué tan independiente es del 1 al 10: "))
            if independencia < 1 or independencia > 10:
                raise ValueError
        except ValueError:
            print("La independencia debe ser un número entre 1 y 10.")
            return
        mascota = Gato(nombre, edad, salud, precio, raza, independencia)
    
    else:
        print("Tipo de mascota no reconocida")
        return None
    
    return mascota 


def registrar_cliente():
    """Registra un cliente en el sistema."""
    nombre = input("Ingresa el nombre del cliente: ").strip()
    direccion = input("Ingresa su dirección: ").strip()
    try:
        telefono = int(input("Teléfono (solo números): "))
    except ValueError:
        print("El teléfono debe contener solo números.")
        return None
    
    cliente = Cliente(nombre, direccion, telefono)
    return cliente

def registrar_producto(inventario):
    """Registra un producto en el inventario."""
    nombre = input("Ingresa el nombre del producto: ").strip().lower()
    try:
        cantidad = int(input("Ingresa la cantidad: ").strip())
        precio = float(input("Ingresa el precio: ").strip())  
    except ValueError:
        print("La cantidad debe ser un número entero y el precio debe ser un número entero o decimal.")
        return None
    
    inventario.agregar_producto(nombre, cantidad, precio)
    print("Producto registrado con éxito")



def registrar_venta(clientes, inventario):
    """Registra una venta de productos a un cliente."""
    nombre_cliente = input("Nombre del cliente: ")
    cliente = next((c for c in clientes if c.nombre == nombre_cliente), None)
    if not cliente:
        print("Cliente no encontrado")
        return
    
    productos = []
    
    while True:
        nombre_producto = input("Nombre del producto (deje vacío para finalizar): ").strip()
        if not nombre_producto:
            break
        producto = next((p for p in inventario.lista_productos if p['nombre'] == nombre_producto), None)    
        if producto:
            try:
                cantidad_vendida = int(input(f"Cantidad de {producto['nombre']} a vender: "))
                if cantidad_vendida > producto['cantidad']:
                    print(f"Stock insuficiente para {producto['nombre']}")
                else:
                    producto['cantidad'] -= cantidad_vendida  # Reducir el stock
                    productos.append({**producto, 'cantidad': cantidad_vendida})  # Guardar cantidad vendida
            except ValueError:
                print("Cantidad inválida")
        else:
            print("Producto no encontrado")
    
    if productos:
        mostrar_resumen_venta(productos)
        confirmacion = input("¿Deseas confirmar la venta? (s/n): ").strip().lower()
        if confirmacion == 's':
            venta = Venta(cliente, productos)
            venta.registrar_venta()
            print("La venta ha sido registrada")
        else:
            print("Venta cancelada")
    else:
        print("No hay productos para registrar")


def mostrar_resumen_venta(productos):
    """Muestra un resumen de los productos en la venta."""
    total = sum([producto['precio'] * producto['cantidad'] for producto in productos])
    print("\nResumen de la venta:")
    for producto in productos:
        print(f"{producto['nombre']} - Cantidad: {producto['cantidad']} - Precio: ${producto['precio']}")
    print(f"Total a pagar: ${total:.2f}")
        
        
def mostrar_menu():
    """Muestra el menú principal."""
    print("\n --- Menú de gestión de 'Patas Felices' --- ")
    print("1. Registrar mascota")
    print("2. Mostrar información sobre mascotas")
    print("3. Registrar cliente")
    print("4. Mostrar información sobre clientes")
    print("5. Registrar producto")
    print("6. Mostrar información sobre productos")
    print("7. Registrar venta")
    print("8. Mostrar ventas totales")
    print("9. Generar alerta de inventario")
    print("10. Salir")
    

def mostrar_mascotas(mascotas):
    """Muestra información sobre todas las mascotas registradas."""
    if not mascotas:
        print("No hay mascotas registradas.")
    else:
        for mascota in mascotas:
            print(f"Nombre: {mascota.nombre}, Edad: {mascota.edad}, Salud: {mascota.salud}, Precio: {mascota.precio}")


def mostrar_clientes(clientes):
    """Muestra información sobre todos los clientes registrados."""
    if not clientes:
        print("No hay clientes registrados.")
    else:
        for cliente in clientes:
            print(cliente.mostrar_informacion())


def mostrar_productos(inventario):
    """Muestra información sobre los productos en el inventario."""
    if not inventario.lista_productos:
        print("No hay productos registrados.")
    else:
        inventario.mostrar_productos()


def generar_alerta_inventario(inventario):
    """Genera alerta sobre productos con bajo stock."""
    stock_alerta = int(input("Ingrese el límite de stock para la alerta: "))
    print(inventario.alerta_stock(stock_alerta))


def main():
    mascotas = []
    clientes = []
    inventario = Inventario()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip().lower()
        
        if opcion == "1":  # Registrar mascota
            mascota = registrar_mascota()
            if mascota:
                mascotas.append(mascota)
                print("Mascota registrada con éxito")
        
        elif opcion == "2":  # Mostrar información sobre mascotas
            for mascota in mascotas:
                print(mascota.mostrar_informacion())
                if isinstance(mascota, Perro) or isinstance(mascota, Gato):
                    print(mascota.mostrar_caracteristicas())
        
        elif opcion == "3":  # Registrar cliente
            cliente = registrar_cliente()
            if cliente:
                clientes.append(cliente)
                print("Cliente registrado correctamente")
        
        elif opcion == "4":  # Mostrar información sobre clientes
            mostrar_clientes(clientes)
        
        elif opcion == "5":  # Registrar producto
            nombre = input("Nombre del producto: ").strip()
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: $"))
                inventario.agregar_producto(nombre, cantidad, precio)
                print("Producto registrado con éxito")
            except ValueError:
                print("Cantidad o precio inválidos")
        
        elif opcion == "6":  # Mostrar información sobre productos
            mostrar_productos(inventario)
        
        elif opcion == "7":  # Registrar venta
            registrar_venta(clientes, inventario)
            
        elif opcion == "8":
            print(Venta.mostrar_ventas_global())
        
        elif opcion == "9":  # Generar alerta de inventario
            generar_alerta_inventario(inventario)
        
        elif opcion == "10":  # Salir del programa
            print("Saliendo del programa. ¡Gracias por usar 'Patas Felices'!")
            break
        
        else:
            print("Opción no válida, intenta de nuevo.")
    
    
'''
# Ejemplo de cómo se pueden usar las funciones
cliente = registrar_cliente()
if cliente:
    print(f"Cliente registrado: {cliente.nombre}, ID: {cliente.id}")

mascota = registrar_mascota()
if mascota:
    print(f"Mascota registrada: {mascota.nombre}, Tipo: {type(mascota).__name__}")
'''   

if __name__ == "__main__":
    main()
