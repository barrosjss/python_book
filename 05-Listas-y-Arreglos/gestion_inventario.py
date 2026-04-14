# 📦 Misión Crítica: Sistema de Gestión de Inventario

inventario = ["Manzanas", "Pan", "Leche"]

def agregar_producto():
    nuevo = input("Nombre del nuevo producto: ").capitalize()
    inventario.append(nuevo)
    print(f"✅ '{nuevo}' ha sido agregado al inventario.")

def ver_inventario():
    print("\n--- LISTA DE PRODUCTOS ---")
    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        for i, producto in enumerate(inventario, start=1):
            print(f"{i}. {producto}")

def buscar_producto():
    busqueda = input("¿Qué producto busca?: ").capitalize()
    if busqueda in inventario:
        posicion = inventario.index(busqueda) + 1
        print(f"🔍 '{busqueda}' se encuentra en la posición {posicion}.")
    else:
        print(f"❌ '{busqueda}' no está en el inventario.")

def eliminar_producto():
    ver_inventario()
    if len(inventario) > 0:
        try:
            indice = int(input("Ingrese el número del producto a eliminar: ")) - 1
            eliminado = inventario.pop(indice)
            print(f"🗑️ '{eliminado}' ha sido eliminado.")
        except:
            print("⚠️ Índice no válido.")

# Programa Principal
while True:
    print("\n--- GESTIÓN DE TIENDA ---")
    print("1. Ver inventario")
    print("2. Agregar producto")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    
    opcion = input("Elija una opción: ")
    
    if opcion == "1":
        ver_inventario()
    elif opcion == "2":
        agregar_producto()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        print("Saliendo del sistema...")
        break
    else:
        print("⚠️ Opción no válida.")
