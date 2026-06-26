=== PARTE 1: NUMPY ===

--- Ejercicio 1 ---
Dimensión original: (12,)
Tipo de dato: int64
Matriz 3x4:
 [[120 150  90 200]
 [ 80 110 140 170]
 [100 130 160 180]]
Interpretación: Filas son las 3 sucursales, columnas son los 4 meses.

--- Ejercicio 2 ---
Ventas totales por sucursal: [560 500 570]
Ventas promedio por mes: [100.         130.         130.         183.33333333]
La sucursal con mayores ventas totales es la sucursal 2 (índice 0-2).
El mes con mayores ventas promedio es el mes 3 (índice 0-3).

--- Ejercicio 3 ---
Promedio general de ventas: 135.83333333333334
Ventas superiores al promedio: [150 200 140 170 160 180]
Matriz con ventas < 100 reemplazadas por 0:
 [[120 150   0 200]
 [  0 110 140 170]
 [100 130 160 180]]

--- Ejercicio 4 ---
Matriz de simulación:
 [[177 147 191 102]
 [140 113 199 162]
 [185  90 165  82]]
Diferencia:
 [[ 57  -3 101 -98]
 [ 60   3  59  -8]
 [ 85 -40   5 -98]]
En promedio, las ventas Aumentaron (10.25).

=== PARTE 2: PANDAS ===

--- Ejercicio 5 ---
DataFrame con Ingreso:
    ID    Producto   Categoria  Precio  Cantidad  Ingreso
0   1      Laptop  Tecnología     800         5     4000
1   2       Mouse  Tecnología      20        50     1000
2   3       Silla       Hogar     100        10     1000
3   4  Escritorio       Hogar     200         7     1400
4   5   Audífonos  Tecnología      50        20     1000

--- Ejercicio 6 ---
Análisis por categoría:
             Ingreso_total  Cantidad_total
Categoria
Hogar                2400              17
Tecnología           6000              75
Categoría más rentable: Tecnología

--- Ejercicio 7 ---
Con nivel de venta:
    ID    Producto   Categoria  Precio  Cantidad  Ingreso Nivel_Venta
0   1      Laptop  Tecnología     800         5     4000        Alto
1   2       Mouse  Tecnología      20        50     1000       Medio
2   3       Silla       Hogar     100        10     1000       Medio
3   4  Escritorio       Hogar     200         7     1400       Medio
4   5   Audífonos  Tecnología      50        20     1000       Medio
Conteo por nivel:
 Nivel_Venta
Medio    4
Alto     1
Name: count, dtype: int64

--- Ejercicio 8 ---
Ingreso promedio: 1680.0
Productos con ingreso superior al promedio (ordenados):
    ID Producto   Categoria  Precio  Cantidad  Ingreso Nivel_Venta
0   1   Laptop  Tecnología     800         5     4000        Alto

--- Ejercicio 9 ---
Dataframe mergeado:
    ID    Producto   Categoria  Precio  Cantidad  Ingreso Nivel_Venta Sucursal
0   1      Laptop  Tecnología     800         5     4000        Alto    Norte
1   2       Mouse  Tecnología      20        50     1000       Medio      Sur
2   3       Silla       Hogar     100        10     1000       Medio   Centro
3   4  Escritorio       Hogar     200         7     1400       Medio    Norte
4   5   Audífonos  Tecnología      50        20     1000       Medio      Sur
Ingreso total por sucursal:
 Sucursal
Centro    1000
Norte     5400
Sur       2000
Name: Ingreso, dtype: int64

--- Ejercicio 10 ---
Sucursal con mayor ingreso: Norte
Categoría que domina por sucursal:
 Sucursal  Categoria
Centro    Hogar         1000
Norte     Hogar         1400
          Tecnología    4000
Sur       Tecnología    2000
Name: Ingreso, dtype: int64
Productos de alto rendimiento en la mejor sucursal:
    ID Producto   Categoria  Precio  Cantidad  Ingreso Nivel_Venta Sucursal
0   1   Laptop  Tecnología     800         5     4000        Alto    Norte