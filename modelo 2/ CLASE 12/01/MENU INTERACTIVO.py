ventas = [
    {"fecha": "12-01-2023", "producto": "Producto_A", "cantidad": 50, "precio": 45.00, "promocion": True},
    {"fecha": "11-01-2023", "producto": "Producto_AX", "cantidad": 160, "precio": 12.00, "promocion": False},
    {"fecha": "10-01-2023", "producto": "Producto_D", "cantidad": 20, "precio": 15.00, "promocion": False},
    {"fecha": "11-01-2023", "producto": "Producto_C", "cantidad": 10, "precio": 140.00, "promocion": False},
    {"fecha": "11-01-2023", "producto": "Producto_D", "cantidad": 1200, "precio": 1.00, "promocion": True}
]

def mostrar_ventas():
    for venta in ventas:
        print(f"Fecha: {venta['fecha']}, Producto: {venta['producto']}, Cantidad: {venta['cantidad']}, Precio: {venta['precio']}, Promoción: {venta['promocion']}")

def agregar_producto():
    fecha = input("Ingrese la fecha (DD-MM-YYYY): ")
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))
    promocion = input("¿Está en promoción? (si/no): ").strip().lower() == "si"
    ventas.append({"fecha": fecha, "producto": producto, "cantidad": cantidad, "precio": precio, "promocion": promocion})
    print("Producto agregado exitosamente.")

def calcular_total_ventas():
    total = sum(venta["cantidad"] * venta["precio"] for venta in ventas)
    print(f"El total de ventas es: {total:.2f}")

def calcular_promedio_ventas():
    total = sum(venta["cantidad"] * venta["precio"] for venta in ventas)
    promedio = total / len(ventas) if ventas else 0
    print(f"El promedio de ventas es: {promedio:.2f}")

def producto_mas_vendido():
    max_producto = max(ventas, key=lambda x: x["cantidad"], default=None)
    if max_producto:
        print(f"El producto más vendido es {max_producto['producto']} con {max_producto['cantidad']} unidades vendidas.")
    else:
        print("No hay ventas registradas.")

def mostrar_productos():
    productos = {venta["producto"] for venta in ventas}
    print("Listado de productos:")
    for producto in productos:
        print(producto)

def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Mostrar el listado de ventas")
        print("2. Añadir un producto")
        print("3. Calcular la suma total de las ventas")
        print("4. Calcular el promedio de ventas")
        print("5. Mostrar el producto más unidades vendidas")
        print("6. Mostrar el listado de productos")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_ventas()
        elif opcion == "2":
            agregar_producto()
        elif opcion == "3":
            calcular_total_ventas()
        elif opcion == "4":
            calcular_promedio_ventas()
        elif opcion == "5":
            producto_mas_vendido()
        elif opcion == "6":
            mostrar_productos()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

# Ejecutar el menú
menu()
