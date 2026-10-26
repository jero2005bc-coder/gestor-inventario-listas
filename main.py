"""Taller 5: inventario en memoria con dos listas paralelas."""

productos = []
cantidades = []


def buscar_indice(nombre):
    """Retorna el índice encontrado o -1; ignora mayúsculas y espacios extra."""
    nombre = " ".join(nombre.split()).casefold()
    for i in range(len(productos)):
        if productos[i].casefold() == nombre:
            return i
    return -1


def leer_nombre():
    while True:
        nombre = " ".join(input("Nombre del producto: ").split())
        if nombre:
            return nombre
        print("El nombre no puede estar vacío.")


def leer_cantidad():
    while True:
        try:
            cantidad = int(input("Cantidad disponible: "))
            if cantidad >= 0:
                return cantidad
            print("La cantidad no puede ser negativa.")
        except ValueError:
            print("Ingrese un número entero, por ejemplo 12.")


def registrar_producto():
    nombre = leer_nombre()
    if buscar_indice(nombre) != -1:
        print("El producto ya existe. Use la opción 4 para modificar su cantidad.")
        return
    cantidad = leer_cantidad()
    productos.append(nombre)
    cantidades.append(cantidad)
    print("Producto registrado:", nombre, "-", cantidad)


def mostrar_inventario():
    if len(productos) == 0:
        print("El inventario está vacío.")
        return
    print("--- INVENTARIO ---")
    for i in range(len(productos)):
        print(i + 1, productos[i], "-", cantidades[i], "unidades")


def buscar_producto():
    indice = buscar_indice(leer_nombre())
    if indice == -1:
        print("El producto no existe.")
    else:
        print("Encontrado:", productos[indice], "-", cantidades[indice], "unidades")


def modificar_cantidad():
    indice = buscar_indice(leer_nombre())
    if indice == -1:
        print("El producto no existe.")
        return
    cantidades[indice] = leer_cantidad()
    print("Cantidad actualizada:", productos[indice], "-", cantidades[indice])


def eliminar_producto():
    indice = buscar_indice(leer_nombre())
    if indice == -1:
        print("El producto no existe.")
        return
    # Eliminar el mismo índice en ambas listas mantiene la relación.
    nombre = productos.pop(indice)
    cantidades.pop(indice)
    print("Producto eliminado:", nombre)


def contar_productos():
    print("Productos diferentes registrados:", len(productos))


def mostrar_mayor():
    if len(productos) == 0:
        print("El inventario está vacío.")
        return
    mayor = max(cantidades)
    print("Mayor cantidad disponible:", mayor)
    # Si hay empate, mostrar todos los productos con esa cantidad.
    for i in range(len(productos)):
        if cantidades[i] == mayor:
            print("-", productos[i], ":", cantidades[i], "unidades")


def menu():
    while True:
        print("\n--- GESTOR DE INVENTARIO ---")
        print("1. Registrar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Modificar cantidad")
        print("5. Eliminar producto")
        print("6. Contar productos diferentes")
        print("7. Mostrar producto con mayor cantidad")
        print("8. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            modificar_cantidad()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            contar_productos()
        elif opcion == "7":
            mostrar_mayor()
        elif opcion == "8":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Elija un número del 1 al 8.")


if __name__ == "__main__":
    menu()
