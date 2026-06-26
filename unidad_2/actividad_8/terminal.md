=== Generando Dataset ===
Archivo estudiantes.csv generado.

--- 1. Exploración inicial ---
Primeras 5 filas:
    ID       Carrera  Edad  PromedioNotas  HorasEstudioSemanal  Asistencia      Ciudad Beca
0   1       Derecho    29            3.6                   10          74    Santiago   No
1   2  Arquitectura    29            6.1                   37          94  Valparaíso   Sí
2   3      Medicina    21            5.8                    4          95  Valparaíso   No
3   4  Arquitectura    21            5.2                    7          81  Concepción   No
4   5  Arquitectura    22            6.5                   33          81    Santiago   No

Estudiantes por carrera:
 Carrera
Informática     210
Derecho         206
Arquitectura    204
Medicina        190
Ingeniería      190
Name: count, dtype: int64

--- 2. Estadísticas descriptivas ---
Promedio de notas por carrera:
 Carrera
Arquitectura    5.282843
Derecho         5.189320
Informática     5.186667
Ingeniería      5.279474
Medicina        5.301053
Name: PromedioNotas, dtype: float64
Media de horas de estudio semanal: 20.06
Porcentaje de estudiantes con beca: 29.90%
Cantidad de alumnos por ciudad:
 Ciudad
Valparaíso      259
Puerto Montt    259
Concepción      258
Santiago        224
Name: count, dtype: int64

--- 3. Visualización ---
Gráficos guardados en 'visualizaciones.png'.

--- 4. Uso de NumPy ---
Percentiles de Asistencia -> 25: 63.0, 50: 75.0, 75: 88.0
Horas de estudio normalizadas (primeros 5): [0.25  0.925 0.1   0.175 0.825]

--- 5. Apriori ---
Conjuntos frecuentes (primeros 5):
    support                           itemsets
0    0.204  frozenset({Carrera_Arquitectura})
1    0.206       frozenset({Carrera_Derecho})
2    0.210   frozenset({Carrera_Informática})
3    0.190    frozenset({Carrera_Ingeniería})
4    0.190      frozenset({Carrera_Medicina})

Reglas de asociación (support > 0.01, conf > 0.1):
                          antecedents                        consequents  ...  certainty  kulczynski
0               frozenset({Beca_No})  frozenset({Carrera_Arquitectura})  ...   0.007161    0.465144
1  frozenset({Carrera_Arquitectura})               frozenset({Beca_No})  ...   0.065512    0.465144
2               frozenset({Beca_Sí})  frozenset({Carrera_Arquitectura})  ...  -0.016790    0.235024
3  frozenset({Carrera_Arquitectura})               frozenset({Beca_Sí})  ...  -0.027943    0.235024
4       frozenset({Carrera_Derecho})               frozenset({Beca_No})  ...  -0.055298    0.442804

[5 rows x 14 columns]

--- 6. KMeans ---
Centroides de los clusters (Edad, PromedioNotas, HorasEstudioSemanal):
 [[24.2428115   5.23003195 34.16932907]
 [23.93195266  5.28224852  6.39053254]
 [23.95415473  5.22578797 20.63323782]]
Gráfico de clusters guardado en 'kmeans_clusters.png'.

Interpretación de los clusters:
Cluster 0: Promedio Edad=24, Notas=5.2, Horas=34.2
Cluster 1: Promedio Edad=24, Notas=5.3, Horas=6.4
Cluster 2: Promedio Edad=24, Notas=5.2, Horas=20.6