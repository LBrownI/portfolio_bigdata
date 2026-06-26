import numpy as np
import pandas as pd

print("=== PARTE 1: NUMPY ===")

# Ejercicio 1: Estructura de datos
print("\n--- Ejercicio 1 ---")
data = np.arange(10, 130, 10)
print("Dimensión original:", data.shape)
print("Tipo de dato:", data.dtype)
matriz = data.reshape(4, 3)
print("Matriz 4x3:\n", matriz)
print("Interpretación: Cada fila representa un equipo y cada columna un periodo (mes).")

# Ejercicio 2: Análisis por equipo
print("\n--- Ejercicio 2 ---")
promedio_equipo = np.mean(matriz, axis=1)
print("Promedio de desempeño por equipo:", promedio_equipo)
promedio_general = np.mean(matriz)
print("Promedio general:", promedio_general)
mejor_equipo = np.argmax(promedio_equipo)
print(f"El equipo con mejor desempeño es el equipo {mejor_equipo} (índice 0-3).")

# Ejercicio 3: Filtrado de rendimiento
print("\n--- Ejercicio 3 ---")
superiores_promedio = matriz[matriz > promedio_general]
print("Evaluaciones superiores al promedio general:", superiores_promedio)
matriz_rendimiento = matriz.copy()
matriz_rendimiento[matriz_rendimiento < 50] = 0
afectados = np.sum(matriz < 50)
print("Matriz con valores inferiores a 50 reemplazados por 0:\n", matriz_rendimiento)
print("Cantidad de valores afectados:", afectados)

# Ejercicio 4: Comparación entre periodos
print("\n--- Ejercicio 4 ---")
nuevos_datos = np.random.randint(10, 130, size=(4, 3))
print("Nuevos datos:\n", nuevos_datos)
diferencia = nuevos_datos - matriz
print("Diferencia entre matrices:\n", diferencia)
cambio_promedio = np.mean(diferencia)
print(f"Cambio promedio: {cambio_promedio}")
if cambio_promedio > 0:
    print("En promedio, el rendimiento Mejoró.")
else:
    print("En promedio, el rendimiento Empeoró.")


print("\n=== PARTE 2: PANDAS ===")

# Ejercicio 5: Creación del DataFrame
print("\n--- Ejercicio 5 ---")
df = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5],
    'Nombre': ['Ana', 'Luis', 'Marta', 'Juan', 'Sofia'],
    'Departamento': ['TI', 'Ventas', 'TI', 'RRHH', 'Ventas'],
    'Edad': [29, 35, 28, 40, 30],
    'Salario': [1200, 1000, 1300, 900, 1100]
})
print("Tipos de datos:\n", df.dtypes)
print("Estadísticas básicas:\n", df.describe())

# Ejercicio 6: Limpieza y transformación
print("\n--- Ejercicio 6 ---")
nuevo_registro = pd.DataFrame([{'ID': 6, 'Nombre': 'Carlos', 'Departamento': 'TI', 'Edad': np.nan, 'Salario': np.nan}])
df = pd.concat([df, nuevo_registro], ignore_index=True)
print("Con nulos:\n", df)
df['Edad'] = df['Edad'].fillna(df['Edad'].mean())
df['Salario'] = df['Salario'].fillna(df['Salario'].mean())
print("Sin nulos:\n", df)
print("¿Existen nulos?:", df.isnull().values.any())

# Ejercicio 7: Análisis por departamento
print("\n--- Ejercicio 7 ---")
agrupado = df.groupby('Departamento').agg(
    Salario_promedio=('Salario', 'mean'),
    Cantidad_empleados=('ID', 'count')
)
print("Análisis por departamento:\n", agrupado)
dep_mayor_salario = agrupado['Salario_promedio'].idxmax()
print("Departamento con mayor salario promedio:", dep_mayor_salario)

# Ejercicio 8: Segmentación de empleados
print("\n--- Ejercicio 8 ---")
def categorizar_salario(s):
    if s < 1000:
        return 'Bajo'
    elif s <= 1200:
        return 'Medio'
    else:
        return 'Alto'

df['Nivel_Salarial'] = df['Salario'].apply(categorizar_salario)
print("Con nivel salarial:\n", df)
print("Conteo por nivel:\n", df['Nivel_Salarial'].value_counts())

# Ejercicio 9: Incorporación de nuevos datos
print("\n--- Ejercicio 9 ---")
df_bonos = pd.DataFrame({
    'ID': [1, 2, 3, 5],
    'Bono': [200, 150, 300, 250]
})
df_completo = pd.merge(df, df_bonos, on='ID', how='left')
print("Empleados sin bono:\n", df_completo[df_completo['Bono'].isnull()])
df_completo['Bono'] = df_completo['Bono'].fillna(0)
df_completo['Ingreso_Total'] = df_completo['Salario'] + df_completo['Bono']
print("DataFrame con Ingreso Total:\n", df_completo)

# Ejercicio 10: Análisis final
print("\n--- Ejercicio 10 ---")
ingreso_dep = df_completo.groupby('Departamento')['Ingreso_Total'].mean()
print("Promedio de ingreso total por departamento:\n", ingreso_dep)
promedio_general_ingreso = df_completo['Ingreso_Total'].mean()
print("Promedio general de ingresos:", promedio_general_ingreso)
print("Empleados con ingreso superior al promedio:\n", df_completo[df_completo['Ingreso_Total'] > promedio_general_ingreso])
print("Interpretación: El área de TI parece ser la más competitiva salarialmente en base a los promedios.")
df_completo.to_csv('resultados_actividad_4.csv', index=False)
