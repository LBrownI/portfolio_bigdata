=== PARTE 1: NUMPY ===

--- Ejercicio 1 ---
Dimensión original: (12,)
Tipo de dato: int64
Matriz 4x3:
 [[ 10  20  30]
 [ 40  50  60]
 [ 70  80  90]
 [100 110 120]]
Interpretación: Cada fila representa un equipo y cada columna un periodo (mes).

--- Ejercicio 2 ---
Promedio de desempeño por equipo: [ 20.  50.  80. 110.]
Promedio general: 65.0
El equipo con mejor desempeño es el equipo 3 (índice 0-3).

--- Ejercicio 3 ---
Evaluaciones superiores al promedio general: [ 70  80  90 100 110 120]
Matriz con valores inferiores a 50 reemplazados por 0:
 [[  0   0   0]
 [  0  50  60]
 [ 70  80  90]
 [100 110 120]]
Cantidad de valores afectados: 4

--- Ejercicio 4 ---
Nuevos datos:
 [[ 98  75  11]
 [123  71  33]
 [113  38 112]
 [ 15  91  37]]
Diferencia entre matrices:
 [[ 88  55 -19]
 [ 83  21 -27]
 [ 43 -42  22]
 [-85 -19 -83]]
Cambio promedio: 3.0833333333333335
En promedio, el rendimiento Mejoró.

=== PARTE 2: PANDAS ===

--- Ejercicio 5 ---
Tipos de datos:
 ID              int64
Nombre            str
Departamento      str
Edad            int64
Salario         int64
dtype: object
Estadísticas básicas:
              ID       Edad      Salario
count  5.000000   5.000000     5.000000
mean   3.000000  32.400000  1100.000000
std    1.581139   5.029911   158.113883
min    1.000000  28.000000   900.000000
25%    2.000000  29.000000  1000.000000
50%    3.000000  30.000000  1100.000000
75%    4.000000  35.000000  1200.000000
max    5.000000  40.000000  1300.000000

--- Ejercicio 6 ---
Con nulos:
    ID  Nombre Departamento  Edad  Salario
0   1     Ana           TI  29.0   1200.0
1   2    Luis       Ventas  35.0   1000.0
2   3   Marta           TI  28.0   1300.0
3   4    Juan         RRHH  40.0    900.0
4   5   Sofia       Ventas  30.0   1100.0
5   6  Carlos           TI   NaN      NaN
Sin nulos:
    ID  Nombre Departamento  Edad  Salario
0   1     Ana           TI  29.0   1200.0
1   2    Luis       Ventas  35.0   1000.0
2   3   Marta           TI  28.0   1300.0
3   4    Juan         RRHH  40.0    900.0
4   5   Sofia       Ventas  30.0   1100.0
5   6  Carlos           TI  32.4   1100.0
¿Existen nulos?: False

--- Ejercicio 7 ---
Análisis por departamento:
               Salario_promedio  Cantidad_empleados
Departamento
RRHH                     900.0                   1
TI                      1200.0                   3
Ventas                  1050.0                   2
Departamento con mayor salario promedio: TI

--- Ejercicio 8 ---
Con nivel salarial:
    ID  Nombre Departamento  Edad  Salario Nivel_Salarial
0   1     Ana           TI  29.0   1200.0          Medio
1   2    Luis       Ventas  35.0   1000.0          Medio
2   3   Marta           TI  28.0   1300.0           Alto
3   4    Juan         RRHH  40.0    900.0           Bajo
4   5   Sofia       Ventas  30.0   1100.0          Medio
5   6  Carlos           TI  32.4   1100.0          Medio
Conteo por nivel:
 Nivel_Salarial
Medio    4
Alto     1
Bajo     1
Name: count, dtype: int64

--- Ejercicio 9 ---
Empleados sin bono:
    ID  Nombre Departamento  Edad  Salario Nivel_Salarial  Bono
3   4    Juan         RRHH  40.0    900.0           Bajo   NaN
5   6  Carlos           TI  32.4   1100.0          Medio   NaN
DataFrame con Ingreso Total:
    ID  Nombre Departamento  Edad  Salario Nivel_Salarial   Bono  Ingreso_Total
0   1     Ana           TI  29.0   1200.0          Medio  200.0         1400.0
1   2    Luis       Ventas  35.0   1000.0          Medio  150.0         1150.0
2   3   Marta           TI  28.0   1300.0           Alto  300.0         1600.0
3   4    Juan         RRHH  40.0    900.0           Bajo    0.0          900.0
4   5   Sofia       Ventas  30.0   1100.0          Medio  250.0         1350.0
5   6  Carlos           TI  32.4   1100.0          Medio    0.0         1100.0

--- Ejercicio 10 ---
Promedio de ingreso total por departamento:
 Departamento
RRHH       900.000000
TI        1366.666667
Ventas    1250.000000
Name: Ingreso_Total, dtype: float64
Promedio general de ingresos: 1250.0
Empleados con ingreso superior al promedio:
    ID Nombre Departamento  Edad  Salario Nivel_Salarial   Bono  Ingreso_Total
0   1    Ana           TI  29.0   1200.0          Medio  200.0         1400.0
2   3  Marta           TI  28.0   1300.0           Alto  300.0         1600.0
4   5  Sofia       Ventas  30.0   1100.0          Medio  250.0         1350.0
Interpretación: El área de TI parece ser la más competitiva salarialmente en base a los promedios.