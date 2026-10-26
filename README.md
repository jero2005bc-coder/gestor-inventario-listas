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

## Listas paralelas y duplicados
`productos[i]` y `cantidades[i]` corresponden al mismo artículo. Ambas listas
siempre tienen igual longitud. Registrar agrega a ambas; modificar solo cambia
la cantidad; eliminar retira el mismo índice de ambas.

Se rechazan duplicados comparando el nombre con `casefold()` e ignorando espacios
sobrantes. Por ejemplo, " ARROZ " y "Arroz" representan el mismo producto.
No se eliminan tildes: "cafe" y "café" se consideran nombres distintos.

## Pruebas realizadas
La transcripción completa está en `evidencias/pruebas.txt`. Las imágenes son
representaciones de la salida real capturada en pruebas automatizadas con entradas
controladas, no capturas manuales de una terminal.

Se comprobó: inventario vacío; registro de Arroz 10, Leche 6 y Pan 15; consulta;
búsqueda existente e inexistente; duplicados; modificación de Leche a 20;
eliminación del primer producto conservando Leche 20 y Pan 15; eliminación
inexistente; conteo y máximo; cantidades negativas, texto, decimales y cero;
nombre vacío; modificación inexistente; empate; opciones inválidas; salida;
eliminación de todos los productos y conteo final cero.

## Explicación del ejercicio de calificaciones
Con 4.0, 3.5, 4.8 y 2.9, el promedio es 3.8, la mayor es 4.8 y la menor 2.9.
Cambiar la segunda nota por 4.2 produce [4.0, 4.2, 4.8, 2.9]: la longitud sigue
siendo 4. Eliminar la primera produce [4.2, 4.8, 2.9]: la longitud baja a 3 y
los índices posteriores se desplazan. `append` agrega, la asignación reemplaza
y `pop` elimina y devuelve el valor. Se resta uno a la posición seleccionada
por el usuario porque los índices empiezan en cero.

## Publicación y entrega pendiente
1. Cree un repositorio público llamado `gestor-inventario-listas` en GitHub.
2. Suba main.py, README.md y la carpeta evidencias; puede incluir calificaciones.py.
3. Ejecute el programa en su equipo y tome capturas manuales si el docente las exige.
4. Complete nombre y grupo en el documento de entrega.
5. Agregue la URL real y clicable del repositorio al PDF y compruebe su acceso
   en una ventana sin sesión iniciada. No hay un repositorio publicado en este paquete.
6. Entregue el PDF actualizado en la plataforma del docente.

El código del inventario no usa archivos, diccionarios, clases, bases de datos ni
librerías externas. Los archivos de evidencias documentan las pruebas; no son
almacenamiento del programa.
