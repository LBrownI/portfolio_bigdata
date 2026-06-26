import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from mlxtend.frequent_patterns import apriori, association_rules
import os

print("=== Generando Dataset ===")
np.random.seed(42)
random.seed(42)

n_records = 1000
ciudades = ["Santiago", "Valparaíso", "Concepción", "Puerto Montt"]
productos = ["Laptop", "Smartphone", "Tablet", "Accesorio"]
metodos_pago = ["Tarjeta", "Transferencia", "Efectivo"]

start_date = datetime(2022, 1, 1)
end_date = datetime(2024, 12, 31)
date_diff = (end_date - start_date).days

datos = {
    "ID": np.arange(1, n_records + 1),
    "ID_Transaccion": np.random.randint(1, 300, n_records), # Simulated transaction ID to group for apriori
    "Edad": np.random.randint(18, 66, n_records),
    "Ciudad": np.random.choice(ciudades, n_records),
    "Producto": np.random.choice(productos, n_records),
    "Precio": np.random.uniform(50, 2000, n_records).round(2),
    "Cantidad": np.random.randint(1, 6, n_records),
    "FechaCompra": [start_date + timedelta(days=random.randint(0, date_diff)) for _ in range(n_records)],
    "MétodoPago": np.random.choice(metodos_pago, n_records)
}

df_ventas = pd.DataFrame(datos)
df_ventas.to_csv('ventas.csv', index=False)
print("Archivo ventas.csv generado.\n")

# 1. Exploración inicial
print("--- 1. Exploración inicial ---")
df = pd.read_csv('ventas.csv')
print("Primeras 10 filas:\n", df.head(10))
print("\nRegistros por ciudad:\n", df['Ciudad'].value_counts())

# 2. Estadísticas descriptivas
print("\n--- 2. Estadísticas descriptivas ---")
print("Promedio de precios por producto:\n", df.groupby('Producto')['Precio'].mean())
print(f"Desviación estándar de las edades: {df['Edad'].std():.2f}")
mas_vendido = df.groupby('Producto')['Cantidad'].sum().idxmax()
print(f"Producto más vendido en cantidad: {mas_vendido}")

# 3. Visualización
print("\n--- 3. Visualización ---")
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
sns.histplot(df['Precio'], bins=20, kde=True)
plt.title("Histograma de Precios")

plt.subplot(1, 3, 2)
sns.countplot(data=df, x='Ciudad')
plt.title("Ventas por Ciudad")
plt.xticks(rotation=45)

plt.subplot(1, 3, 3)
sns.scatterplot(data=df, x='Precio', y='Cantidad')
plt.title("Precio vs Cantidad")

plt.tight_layout()
plt.savefig("visualizaciones.png")
print("Gráficos guardados en 'visualizaciones.png'.")
plt.close()

# 4. Uso de NumPy
print("\n--- 4. Uso de NumPy ---")
precios_np = df['Precio'].values
precios_norm = (precios_np - precios_np.min()) / (precios_np.max() - precios_np.min())
print("Precios normalizados (primeros 5):", precios_norm[:5])
p25, p50, p75 = np.percentile(precios_np, [25, 50, 75])
print(f"Percentiles del Precio -> 25: {p25}, 50: {p50}, 75: {p75}")

# 5. Apriori
print("\n--- 5. Apriori ---")
# Generar matriz de transacciones: agrupar por ID_Transaccion y hacer un hot encoding
# Usamos map() o applymap()
cesta = df.groupby(['ID_Transaccion', 'Producto'])['Cantidad'].sum().unstack().reset_index().fillna(0).set_index('ID_Transaccion')
def encode_units(x):
    if x <= 0: return 0
    if x >= 1: return 1
cesta_sets = cesta.map(encode_units) if hasattr(cesta, 'map') else cesta.applymap(encode_units)

# Aplicar Apriori
frequent_itemsets = apriori(cesta_sets, min_support=0.05, use_colnames=True)
print("Conjuntos frecuentes:\n", frequent_itemsets.head())
if not frequent_itemsets.empty:
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6, num_itemsets=len(frequent_itemsets))
    print("\nReglas de asociación (support > 0.05, conf > 0.6):\n", rules)
else:
    print("No se encontraron itemsets frecuentes.")

# 6. KMeans
print("\n--- 6. KMeans ---")
X = df[['Edad', 'Precio', 'Cantidad']]
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(X)

print("Centroides de los clusters (Edad, Precio, Cantidad):\n", kmeans.cluster_centers_)

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Edad', y='Precio', hue='Cluster', palette='viridis', style='Cantidad')
plt.title("Clustering de Clientes (K=3)")
plt.savefig("kmeans_clusters.png")
print("Gráfico de clusters guardado en 'kmeans_clusters.png'.")
plt.close()

print("\nInterpretación de los clusters (Ejemplo general basado en Edad, Precio y Cantidad):")
for i, center in enumerate(kmeans.cluster_centers_):
    print(f"Cluster {i}: Promedio Edad={center[0]:.0f}, Precio={center[1]:.0f}, Cantidad={center[2]:.1f}")
