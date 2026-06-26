import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

print("=== Ejercicio Actividad K-Means ===")

# Paso 2: Cargar el archivo
df = pd.read_csv('clientes.csv')

# Paso 3: Analizar los datos
print("Primeras filas:\n", df.head())
print("\nTipos de datos:\n", df.dtypes)

# Paso 4: Seleccionar variables numéricas
X = df[['Edad', 'Gasto_Mensual']]

# Paso 5: Normalizar los datos
scaler = StandardScaler()
X_norm = scaler.fit_transform(X)

# Paso 6: Aplicar KMeans con 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_norm)

# Paso 7: Agregar el cluster al DataFrame original
df['Cluster'] = clusters
print("\nDatos con Clusters asignados:\n", df)

# Obtener centroides en escala original
centroides_norm = kmeans.cluster_centers_
centroides_orig = scaler.inverse_transform(centroides_norm)

print("\nCentroides de los clusters (Edad, Gasto_Mensual):")
for i, center in enumerate(centroides_orig):
    print(f"Cluster {i}: Edad = {center[0]:.1f}, Gasto = {center[1]:.1f}")

# Paso 8: Visualizar
plt.figure(figsize=(8, 6))

colors = ['r', 'g', 'b']
for i in range(3):
    cluster_data = df[df['Cluster'] == i]
    plt.scatter(cluster_data['Edad'], cluster_data['Gasto_Mensual'], 
                c=colors[i], label=f'Cluster {i}', s=100, alpha=0.7)

# Visualizar centroides
plt.scatter(centroides_orig[:, 0], centroides_orig[:, 1], 
            c='black', marker='X', s=200, label='Centroides')

plt.title('Segmentación de Clientes (K-Means)')
plt.xlabel('Edad')
plt.ylabel('Gasto Mensual')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig('kmeans_clientes_plot.png')
print("\nGráfico guardado en 'kmeans_clientes_plot.png'.")

df.to_csv('clientes_con_clusters.csv', index=False)
