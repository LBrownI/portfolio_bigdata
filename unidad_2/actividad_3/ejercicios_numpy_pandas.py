import numpy as np
import pandas as pd

print("=== PARTE 1: NUMPY ===")

# Ejercicio 1: Shape y transformación de arreglos
print("\n--- Ejercicio 1 ---")
arr = np.arange(1, 21)
print("Shape original:", arr.shape)
print("Dtype:", arr.dtype)
mat = arr.reshape(4, 5)
print("Matriz 4x5:\n", mat)
print("Segunda fila:", mat[1, :])
print("Tercera columna:", mat[:, 2])

# Ejercicio 2: Manipulación de datos
print("\n--- Ejercicio 2 ---")
arr2 = np.array([5, 10, 15, 20, 25, 30])
arr2_mult = arr2 * 3
print("Multiplicado por 3:", arr2_mult)
arr2_mult[arr2_mult > 20] = -1
print("Reemplazar > 20 por -1:", arr2_mult)
positivos = arr2_mult[arr2_mult > 0]
print("Valores positivos resultantes:", positivos)

# Ejercicio 3: Matrices y operaciones
print("\n--- Ejercicio 3 ---")
matA = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matB = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("Suma entre matrices:\n", matA + matB)
print("Multiplicación elemento a elemento:\n", matA * matB)
print("Suma total matA:", np.sum(matA))
print("Suma total matB:", np.sum(matB))

# Ejercicio 4: Estadística básica
print("\n--- Ejercicio 4 ---")
arr_rand = np.random.randint(1, 50, size=10)
print("Arreglo original:", arr_rand)
promedio = np.mean(arr_rand)
print("Promedio:", promedio)
print("Máximo:", np.max(arr_rand))
print("Mínimo:", np.min(arr_rand))
arr_sorted = np.sort(arr_rand)
print("Ordenado de menor a mayor:", arr_sorted)
mayores_promedio = np.sum(arr_rand > promedio)
print("Cantidad mayores al promedio:", mayores_promedio)

# Ejercicio 5: Integración simple
print("\n--- Ejercicio 5 ---")
mat_rand = np.random.randint(1, 100, size=(5, 4))
print("Matriz 5x4:\n", mat_rand)
promedios_fila = np.mean(mat_rand, axis=1)
print("Promedio por fila:", promedios_fila)
fila_mayor_promedio = np.argmax(promedios_fila)
print("Fila con mayor promedio (índice):", fila_mayor_promedio)
print("Fila con mayor promedio:", mat_rand[fila_mayor_promedio])


print("\n=== PARTE 2: PANDAS ===")

# Ejercicio 6: Creación y exploración
print("\n--- Ejercicio 6 ---")
df_est = pd.DataFrame({
    'Nombre': ['Juan', 'Ana', 'Pedro', 'Laura', 'Carlos'],
    'Edad': [20, 22, 21, 23, 20],
    'Carrera': ['Ing', 'Med', 'Der', 'Ing', 'Arq']
})
print("Primeras filas:\n", df_est.head())
print("Tipos de datos:\n", df_est.dtypes)
print("Resumen estadístico:\n", df_est.describe())

# Ejercicio 7: Agregar y modificar datos
print("\n--- Ejercicio 7 ---")
df_est['Promedio'] = [5.5, 3.8, 4.2, 6.0, 3.5]
df_est['Estado'] = np.where(df_est['Promedio'] >= 4, 'Aprobado', 'Reprobado')
print("DataFrame con Promedio y Estado:\n", df_est)
print("Solo aprobados:\n", df_est[df_est['Estado'] == 'Aprobado'])

# Ejercicio 8: Agrupación y agregación
print("\n--- Ejercicio 8 ---")
data = {
    "Carrera": ["Ing", "Ing", "Med", "Med", "Ing"],
    "Promedio": [5.0, 4.5, 6.0, 5.5, 3.8]
}
df_agrupar = pd.DataFrame(data)
resumen_carrera = df_agrupar.groupby('Carrera').agg(
    Promedio_notas=('Promedio', 'mean'),
    Cantidad_estudiantes=('Carrera', 'count')
)
print("Resumen por carrera:\n", resumen_carrera)

# Ejercicio 9: Agregar filas y análisis
print("\n--- Ejercicio 9 ---")
nuevos = pd.DataFrame({
    "Carrera": ["Der", "Arq"],
    "Promedio": [4.0, 6.5]
})
df_agrupar = pd.concat([df_agrupar, nuevos], ignore_index=True)
prom_general = df_agrupar['Promedio'].mean()
print("Promedio general:", prom_general)
print("Estudiantes sobre el promedio general:\n", df_agrupar[df_agrupar['Promedio'] > prom_general])

# Ejercicio 10: Combinación de DataFrames
print("\n--- Ejercicio 10 ---")
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Nombre': ['Alice', 'Bob', 'Charlie', 'David']
})
df2 = pd.DataFrame({
    'ID': [3, 4, 5, 6],
    'Carrera': ['Ing', 'Med', 'Arq', 'Der']
})
df_merge = pd.merge(df1, df2, on='ID', how='outer', indicator=True)
print("Merge realizado:\n", df_merge)
sin_coincidencia = df_merge[df_merge['_merge'] != 'both']
print("IDs sin coincidencia:\n", sin_coincidencia)
