# Gestor de inventario con listas

Proyecto del Taller 5 de Lógica de Programación.

## Objetivo
Administrar nombres y cantidades de una tienda usando listas, índices, ciclos,
condicionales y funciones. Los datos solo existen durante la ejecución.

## Requisitos y ejecución
Python 3, sin instalaciones adicionales. Descomprima el paquete y abra una terminal
en esta carpeta. Ejecute:

```bash
python main.py
```

Si su sistema lo requiere, use `python3 main.py`. Para la parte guiada:

```bash
python calificaciones.py
```

## Instrucciones de uso
1. Registrar un producto: escriba su nombre y una cantidad entera no negativa.
2. Mostrar todos los productos con su cantidad.
3. Buscar por nombre completo; se ignoran mayúsculas y espacios adicionales.
4. Modificar: reemplaza la cantidad del producto existente (no suma unidades).
5. Eliminar: retira el nombre y su cantidad del mismo índice.
6. Contar productos diferentes, incluidos los que tienen cero unidades.
7. Consultar la mayor cantidad; si hay empate, se muestran todos los empatados.
8. Salir. Al cerrar se pierden los datos.

## Funciones implementadas
- `buscar_indice(nombre)`: recorre los nombres y devuelve el índice o -1.
- `leer_nombre()`: impide nombres vacíos y normaliza los espacios.
- `leer_cantidad()`: solicita un entero mayor o igual a cero.
- `registrar_producto()`: comprueba duplicados y agrega en ambas listas.
- `mostrar_inventario()`: recorre las listas usando el mismo índice.
- `buscar_producto()`: informa si un nombre existe y muestra su cantidad.
- `modificar_cantidad()`: verifica existencia y reemplaza la cantidad.
- `eliminar_producto()`: ejecuta pop en ambas listas con el mismo índice.
- `contar_productos()`: usa len(productos).
- `mostrar_mayor()`: verifica que haya datos y obtiene el máximo.
- `menu()`: repite el menú hasta seleccionar 8 y controla opciones inválidas.





