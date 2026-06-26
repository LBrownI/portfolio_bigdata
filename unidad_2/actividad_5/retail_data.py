import numpy as np
import pandas as pd

print("=== PARTE 1: NUMPY ===")

# Ejercicio 1: Estructura de ventas
print("\n--- Ejercicio 1 ---")
ventas = np.array([120, 150, 90, 200, 80, 110, 140, 170, 100, 130, 160, 180])
print("Dimensión original:", ventas.shape)
print("Tipo de dato:", ventas.dtype)
matriz = ventas.reshape(3, 4)
print("Matriz 3x4:\n", matriz)
print("Interpretación: Filas son las 3 sucursales, columnas son los 4 meses.")

# Ejercicio 2: Análisis de ventas
print("\n--- Ejercicio 2 ---")
ventas_sucursal = np.sum(matriz, axis=1)
print("Ventas totales por sucursal:", ventas_sucursal)
ventas_mes = np.mean(matriz, axis=0)
print("Ventas promedio por mes:", ventas_mes)
sucursal_mayor = np.argmax(ventas_sucursal)
print(f"La sucursal con mayores ventas totales es la sucursal {sucursal_mayor} (índice 0-2).")
mes_mayor = np.argmax(ventas_mes)
print(f"El mes con mayores ventas promedio es el mes {mes_mayor} (índice 0-3).")

# Ejercicio 3: Evaluación de desempeño
print("\n--- Ejercicio 3 ---")
prom_ventas = np.mean(matriz)
print("Promedio general de ventas:", prom_ventas)
print("Ventas superiores al promedio:", matriz[matriz > prom_ventas])
matriz_filtrada = np.where(matriz < 100, 0, matriz)
print("Matriz con ventas < 100 reemplazadas por 0:\n", matriz_filtrada)

# Ejercicio 4: Comparación de escenarios
print("\n--- Ejercicio 4 ---")
simulacion = np.random.randint(80, 200, size=(3, 4))
diferencia = simulacion - matriz
print("Matriz de simulación:\n", simulacion)
print("Diferencia:\n", diferencia)
cambio_prom = np.mean(diferencia)
if cambio_prom > 0:
    print(f"En promedio, las ventas Aumentaron ({cambio_prom}).")
else:
    print(f"En promedio, las ventas Disminuyeron ({cambio_prom}).")

print("\n=== PARTE 2: PANDAS ===")

# Ejercicio 5: Creación de DataFrame
print("\n--- Ejercicio 5 ---")
df_ventas = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5],
    'Producto': ['Laptop', 'Mouse', 'Silla', 'Escritorio', 'Audífonos'],
    'Categoria': ['Tecnología', 'Tecnología', 'Hogar', 'Hogar', 'Tecnología'],
    'Precio': [800, 20, 100, 200, 50],
    'Cantidad': [5, 50, 10, 7, 20]
})
df_ventas['Ingreso'] = df_ventas['Precio'] * df_ventas['Cantidad']
print("DataFrame con Ingreso:\n", df_ventas)

# Ejercicio 6: Análisis por categoría
print("\n--- Ejercicio 6 ---")
agrupado = df_ventas.groupby('Categoria').agg(
    Ingreso_total=('Ingreso', 'sum'),
    Cantidad_total=('Cantidad', 'sum')
)
print("Análisis por categoría:\n", agrupado)
cat_rentable = agrupado['Ingreso_total'].idxmax()
print("Categoría más rentable:", cat_rentable)

# Ejercicio 7: Segmentación de productos
print("\n--- Ejercicio 7 ---")
def nivel_venta(i):
    if i < 500:
        return 'Bajo'
    elif i <= 2000:
        return 'Medio'
    else:
        return 'Alto'

df_ventas['Nivel_Venta'] = df_ventas['Ingreso'].apply(nivel_venta)
print("Con nivel de venta:\n", df_ventas)
print("Conteo por nivel:\n", df_ventas['Nivel_Venta'].value_counts())

# Ejercicio 8: Agregación y filtrado
print("\n--- Ejercicio 8 ---")
ingreso_prom = df_ventas['Ingreso'].mean()
print("Ingreso promedio:", ingreso_prom)
superiores = df_ventas[df_ventas['Ingreso'] > ingreso_prom].sort_values(by='Ingreso', ascending=False)
print("Productos con ingreso superior al promedio (ordenados):\n", superiores)

# Ejercicio 9: Combinación de datos
print("\n--- Ejercicio 9 ---")
df_sucursales = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5],
    'Sucursal': ['Norte', 'Sur', 'Centro', 'Norte', 'Sur']
})
df_merged = pd.merge(df_ventas, df_sucursales, on='ID')
print("Dataframe mergeado:\n", df_merged)
ingreso_sucursal = df_merged.groupby('Sucursal')['Ingreso'].sum()
print("Ingreso total por sucursal:\n", ingreso_sucursal)

# Ejercicio 10: Análisis final
print("\n--- Ejercicio 10 ---")
mejor_sucursal = ingreso_sucursal.idxmax()
print("Sucursal con mayor ingreso:", mejor_sucursal)
print("Categoría que domina por sucursal:\n", df_merged.groupby(['Sucursal', 'Categoria'])['Ingreso'].sum())
alto_rendimiento = df_merged[(df_merged['Sucursal'] == mejor_sucursal) & (df_merged['Nivel_Venta'] == 'Alto')]
print("Productos de alto rendimiento en la mejor sucursal:\n", alto_rendimiento)
df_merged.to_csv('resultados_actividad_5.csv', index=False)
