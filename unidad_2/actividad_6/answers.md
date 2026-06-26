=== CASO PRACTICO INTEGRADOR: TechRetail SpA ===

--- PARTE 1: Procesamiento Numérico (NumPy) ---
Matriz de Desempeño (3x4):
 [[ 80  90  75  85]
 [ 60  70  65  75]
 [ 95  85  90 100]]
Promedio por equipo: [82.5 67.5 92.5]
Promedio por mes: [78.33333333 81.66666667 76.66666667 86.66666667]
Promedio general: 80.83333333333333
Equipo con mejor desempeño: Equipo 3
Mes con menor desempeño: Mes 3
Valores sobre el promedio general: [ 90  85  95  85  90 100]
Matriz con valores < 70 reemplazados por 0:
 [[ 80  90  75  85]
 [  0  70   0  75]
 [ 95  85  90 100]]

--- PARTE 2: Gestión de Datos (Pandas) ---
DataFrame con Ingreso:
    ID    Producto   Categoria  Precio  Cantidad Sucursal  Ingreso
0   1      Laptop  Tecnología     800         5    Norte     4000
1   2       Mouse  Tecnología      20        50      Sur     1000
2   3     Teclado  Tecnología      50        30   Centro     1500
3   4     Monitor  Tecnología     300        10    Norte     3000
4   5       Silla       Hogar     120        15      Sur     1800
5   6  Escritorio       Hogar     250         8   Centro     2000
Ingreso total por categoría:
 Categoria
Hogar         3800
Tecnología    9500
Name: Ingreso, dtype: int64
Ingreso total por sucursal:
 Sucursal
Centro    3500
Norte     7000
Sur       2800
Name: Ingreso, dtype: int64
Promedio de ingreso por producto: 2216.6666666666665
Cantidad total vendida por categoría:
 Categoria
Hogar         23
Tecnología    95
Name: Cantidad, dtype: int64
DataFrame con Segmentación Nivel_Venta:
    ID    Producto   Categoria  Precio  Cantidad Sucursal  Ingreso Nivel_Venta
0   1      Laptop  Tecnología     800         5    Norte     4000        Alto
1   2       Mouse  Tecnología      20        50      Sur     1000       Medio
2   3     Teclado  Tecnología      50        30   Centro     1500       Medio
3   4     Monitor  Tecnología     300        10    Norte     3000       Medio
4   5       Silla       Hogar     120        15      Sur     1800       Medio
5   6  Escritorio       Hogar     250         8   Centro     2000       Medio
Productos con ingresos superiores al promedio:
    ID Producto   Categoria  Precio  Cantidad Sucursal  Ingreso Nivel_Venta
0   1   Laptop  Tecnología     800         5    Norte     4000        Alto
3   4  Monitor  Tecnología     300        10    Norte     3000       Medio

--- PARTE 3 y 4: Integración y Conclusiones ---

CONCLUSIONES:
1. ¿Qué área de la empresa tiene mejor rendimiento?
   Basado en el desempeño de los equipos (Parte 1), el Equipo 3 es el de mayor rendimiento, con un promedio de 92.50.

2. ¿Qué sucursal presenta mayor desempeño comercial?
   La sucursal 'Norte' tiene el mayor ingreso total con 7000.

3. ¿Existe relación entre desempeño y ventas?
   Se puede inferir si asumimos que cada equipo está ligado a una sucursal. Por ejemplo, el Equipo 3 tiene el mayor rendimiento (92.5), lo que podría asociarse a una sucursal, mientras que la sucursal 'Norte' genera los mayores ingresos (7000).
   Para hacer esta relación formal se requiere que el cruce de datos contenga las sucursales asignadas a los equipos.

4. ¿Qué decisiones recomendarías a la gerencia?
   A) Potenciar el abastecimiento y las promociones en la categoría 'Tecnología', que actualmente domina en ventas de manera significativa.
   B) Investigar por qué el mes 3 presentó una caída de desempeño en los equipos y tomar medidas correctivas (por ej. capacitaciones) para las evaluaciones que quedaron con nota bajo 70.