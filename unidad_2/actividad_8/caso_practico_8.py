import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from mlxtend.frequent_patterns import apriori, association_rules
import os

print("=== Generando Dataset ===")
np.random.seed(42)
random.seed(42)

n_records = 1000
carreras = ["Informática", "Ingeniería", "Medicina", "Derecho", "Arquitectura"]
ciudades = ["Santiago", "Valparaíso", "Concepción", "Puerto Montt"]
becas = ["Sí", "No"]

datos = {
    "ID": np.arange(1, n_records + 1),
    "Carrera": np.random.choice(carreras, n_records),
    "Edad": np.random.randint(18, 31, n_records),
    "PromedioNotas": np.random.uniform(3.5, 7.0, n_records).round(1),
    "HorasEstudioSemanal": np.random.randint(0, 41, n_records),
    "Asistencia": np.random.randint(50, 101, n_records),
    "Ciudad": np.random.choice(ciudades, n_records),
    "Beca": np.random.choice(becas, n_records, p=[0.3, 0.7]) # Just simulating 30% becas
}

df_est = pd.DataFrame(datos)
df_est.to_csv('estudiantes.csv', index=False)
print("Archivo estudiantes.csv generado.\n")

# 1. Exploración inicial
print("--- 1. Exploración inicial ---")
df = pd.read_csv('estudiantes.csv')
print("Primeras 5 filas:\n", df.head(5))
print("\nEstudiantes por carrera:\n", df['Carrera'].value_counts())

# 2. Estadísticas descriptivas
print("\n--- 2. Estadísticas descriptivas ---")
print("Promedio de notas por carrera:\n", df.groupby('Carrera')['PromedioNotas'].mean())
print(f"Media de horas de estudio semanal: {df['HorasEstudioSemanal'].mean():.2f}")
pct_beca = (df['Beca'] == 'Sí').mean() * 100
print(f"Porcentaje de estudiantes con beca: {pct_beca:.2f}%")
print("Cantidad de alumnos por ciudad:\n", df['Ciudad'].value_counts())

# 3. Visualización
print("\n--- 3. Visualización ---")
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
sns.histplot(df['HorasEstudioSemanal'], bins=20, kde=True)
plt.title("Histograma Horas de Estudio")

plt.subplot(1, 3, 2)
prom_por_ciudad = df.groupby('Ciudad')['PromedioNotas'].mean().reset_index()
sns.barplot(data=prom_por_ciudad, x='Ciudad', y='PromedioNotas')
plt.title("Promedio de Notas por Ciudad")
plt.xticks(rotation=45)
plt.ylim(3.5, 7.0)

plt.subplot(1, 3, 3)
sns.scatterplot(data=df, x='HorasEstudioSemanal', y='PromedioNotas', alpha=0.5)
plt.title("Horas Estudio vs Promedio Notas")

plt.tight_layout()
plt.savefig("visualizaciones.png")
print("Gráficos guardados en 'visualizaciones.png'.")
plt.close()

# 4. Uso de NumPy
print("\n--- 4. Uso de NumPy ---")
asistencia_np = df['Asistencia'].values
p25, p50, p75 = np.percentile(asistencia_np, [25, 50, 75])
print(f"Percentiles de Asistencia -> 25: {p25}, 50: {p50}, 75: {p75}")

horas_np = df['HorasEstudioSemanal'].values
horas_norm = (horas_np - horas_np.min()) / (horas_np.max() - horas_np.min())
print("Horas de estudio normalizadas (primeros 5):", horas_norm[:5])

# 5. Apriori
print("\n--- 5. Apriori ---")
# One hot encoding for Carrera and Beca to find association rules
df_apriori = pd.get_dummies(df[['Carrera', 'Beca']])
# Convert to boolean for apriori
df_apriori = df_apriori.astype(bool)

frequent_itemsets = apriori(df_apriori, min_support=0.01, use_colnames=True)
print("Conjuntos frecuentes (primeros 5):\n", frequent_itemsets.head())
if not frequent_itemsets.empty:
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.1, num_itemsets=len(frequent_itemsets))
    print("\nReglas de asociación (support > 0.01, conf > 0.1):\n", rules.head())
else:
    print("No se encontraron itemsets frecuentes.")

# 6. KMeans
print("\n--- 6. KMeans ---")
X = df[['Edad', 'PromedioNotas', 'HorasEstudioSemanal']]
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(X)

print("Centroides de los clusters (Edad, PromedioNotas, HorasEstudioSemanal):\n", kmeans.cluster_centers_)

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='HorasEstudioSemanal', y='PromedioNotas', hue='Cluster', palette='viridis', style='Edad')
plt.title("Clustering de Estudiantes (K=3)")
plt.savefig("kmeans_clusters.png")
print("Gráfico de clusters guardado en 'kmeans_clusters.png'.")
plt.close()

print("\nInterpretación de los clusters:")
for i, center in enumerate(kmeans.cluster_centers_):
    print(f"Cluster {i}: Promedio Edad={center[0]:.0f}, Notas={center[1]:.1f}, Horas={center[2]:.1f}")
