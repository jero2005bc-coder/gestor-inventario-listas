"""Parte 2: registro, consulta, modificación y eliminación de notas."""


def leer_nota():
    while True:
        try:
            nota = float(input("Ingrese una nota entre 0 y 5: "))
            if 0 <= nota <= 5:
                return nota
            print("La nota debe estar entre 0 y 5.")
        except ValueError:
            print("Ingrese un número; use punto para los decimales.")


def leer_posicion(mensaje, longitud):
    while True:
        try:
            posicion = int(input(mensaje))
            if 1 <= posicion <= longitud:
                return posicion - 1
            print("La posición no es válida.")
        except ValueError:
            print("Ingrese una posición entera.")


def main():
    notas = []
    for i in range(4):
        notas.append(leer_nota())
    print("\n--- NOTAS REGISTRADAS ---")
    for i in range(len(notas)):
        print("Nota", i + 1, ":", notas[i])
    print("Promedio:", round(sum(notas) / len(notas), 2))
    print("Nota mayor:", max(notas))
    print("Nota menor:", min(notas))
    indice = leer_posicion("Posición que desea modificar (1-4): ", len(notas))
    notas[indice] = leer_nota()
    print("Notas después de modificar:", notas)
    indice = leer_posicion("Posición que desea eliminar (1-4): ", len(notas))
    print("Nota eliminada:", notas.pop(indice))
    print("Notas finales:", notas)


if __name__ == "__main__":
    main()
