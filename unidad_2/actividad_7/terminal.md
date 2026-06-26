=== Generando Dataset ===
Archivo ventas.csv generado.

--- 1. Exploración inicial ---
Primeras 10 filas:
    ID  ID_Transaccion  Edad        Ciudad  ...   Precio  Cantidad  FechaCompra     MétodoPago
0   1             103    57    Concepción  ...  1459.28         4   2022-08-17       Efectivo      
1   2             271    36    Concepción  ...  1400.44         2   2022-02-21  Transferencia      
2   3             107    35    Concepción  ...   312.15         2   2023-07-18        Tarjeta      
3   4              72    18  Puerto Montt  ...   633.82         3   2023-05-17  Transferencia      
4   5             189    31      Santiago  ...   749.50         4   2023-04-03        Tarjeta      
5   6              21    64      Santiago  ...  1618.65         2   2022-10-13  Transferencia      
6   7             103    19    Valparaíso  ...   593.58         2   2022-07-29  Transferencia      
7   8             122    45    Concepción  ...   460.87         4   2022-06-28       Efectivo      
8   9             215    47    Valparaíso  ...  1917.02         5   2024-05-14  Transferencia      
9  10              88    55    Valparaíso  ...    67.28         4   2022-03-07  Transferencia      

[10 rows x 9 columns]

Registros por ciudad:
 Ciudad
Puerto Montt    266
Valparaíso      261
Santiago        248
Concepción      225
Name: count, dtype: int64

--- 2. Estadísticas descriptivas ---
Promedio de precios por producto:
 Producto
Accesorio      981.926157
Laptop        1070.464525
Smartphone    1023.546150
Tablet        1028.648125
Name: Precio, dtype: float64
Desviación estándar de las edades: 13.81
Producto más vendido en cantidad: Tablet

--- 3. Visualización ---
Gráficos guardados en 'visualizaciones.png'.

--- 4. Uso de NumPy ---
Precios normalizados (primeros 5): [0.72350628 0.69329815 0.13457609 0.29971969 0.35910916]        
Percentiles del Precio -> 25: 538.1624999999999, 50: 1038.63, 75: 1510.51

--- 5. Apriori ---
C:\Users\WindowsLOQ\AppData\Roaming\Python\Python314\site-packages\mlxtend\frequent_patterns\fpcommon.py:175: DeprecationWarning: DataFrames with non-bool types result in worse computationalperformance and their support might be discontinued in the future.Please use a DataFrame with bool type    
  warnings.warn(
Conjuntos frecuentes:
     support                        itemsets
0  0.588028          frozenset({Accesorio})
1  0.616197             frozenset({Laptop})
2  0.531690         frozenset({Smartphone})
3  0.570423             frozenset({Tablet})
4  0.366197  frozenset({Accesorio, Laptop})

Reglas de asociación (support > 0.05, conf > 0.6):
                                   antecedents          consequents  ...  certainty  kulczynski
0                      frozenset({Accesorio})  frozenset({Laptop})  ...   0.017085    0.608520     
1                     frozenset({Smartphone})  frozenset({Laptop})  ...  -0.035300    0.561325     
2                         frozenset({Tablet})  frozenset({Laptop})  ...   0.018915    0.600300     
3          frozenset({Accesorio, Smartphone})  frozenset({Laptop})  ...   0.038445    0.466905     
4              frozenset({Tablet, Accesorio})  frozenset({Laptop})  ...   0.065417    0.489224     
5             frozenset({Tablet, Smartphone})  frozenset({Laptop})  ...   0.255570    0.514286     
6             frozenset({Smartphone, Laptop})  frozenset({Tablet})  ...   0.079085    0.471951     
7  frozenset({Tablet, Accesorio, Smartphone})  frozenset({Laptop})  ...   0.317606    0.457619     

[8 rows x 14 columns]

--- 6. KMeans ---
Centroides de los clusters (Edad, Precio, Cantidad):
 [[  41.46688742 1003.17718543    3.0794702 ]
 [  42.09063444  366.16522659    3.081571  ]
 [  41.7493188  1641.4672752     3.01089918]]
Gráfico de clusters guardado en 'kmeans_clusters.png'.

Interpretación de los clusters (Ejemplo general basado en Edad, Precio y Cantidad):
Cluster 0: Promedio Edad=41, Precio=1003, Cantidad=3.1
Cluster 1: Promedio Edad=42, Precio=366, Cantidad=3.1
Cluster 2: Promedio Edad=42, Precio=1641, Cantidad=3.0