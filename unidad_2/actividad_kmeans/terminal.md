=== Ejercicio Actividad K-Means ===
Primeras filas:
   Cliente  Edad  Gasto_Mensual
0      C1    22            200
1      C2    25            220
2      C3    23            210
3      C4    35            400
4      C5    38            420

Tipos de datos:
 Cliente            str
Edad             int64
Gasto_Mensual    int64
dtype: object

Datos con Clusters asignados:
   Cliente  Edad  Gasto_Mensual  Cluster
0      C1    22            200        2
1      C2    25            220        2
2      C3    23            210        2
3      C4    35            400        0
4      C5    38            420        0
5      C6    40            450        0
6      C7    45            900        1
7      C8    47            950        1
8      C9    50            980        1
9     C10    46            920        1

Centroides de los clusters (Edad, Gasto_Mensual):
Cluster 0: Edad = 37.7, Gasto = 423.3
Cluster 1: Edad = 47.0, Gasto = 937.5
Cluster 2: Edad = 23.3, Gasto = 210.0

Gráfico guardado en 'kmeans_clientes_plot.png'.