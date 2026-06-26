import numpy as np
import pandas as pd

print("=== CASO PRACTICO INTEGRADOR: TechRetail SpA ===")

print("\n--- PARTE 1: Procesamiento Numérico (NumPy) ---")
desempeno = np.array([80, 90, 75, 85, 60, 70, 65, 75, 95, 85, 90, 100])

# Reorganiza los datos en una matriz de 3 equipos x 4 meses
matriz_desempeno = desempeno.reshape(3, 4)
print("Matriz de Desempeño (3x4):\n", matriz_desempeno)

# Calcula promedios
prom_equipo = np.mean(matriz_desempeno, axis=1)
print("Promedio por equipo:", prom_equipo)

prom_mes = np.mean(matriz_desempeno, axis=0)
print("Promedio por mes:", prom_mes)

prom_general = np.mean(matriz_desempeno)
print("Promedio general:", prom_general)

# Identifica equipo mejor y mes peor
mejor_equipo = np.argmax(prom_equipo)
print(f"Equipo con mejor desempeño: Equipo {mejor_equipo + 1}")

peor_mes = np.argmin(prom_mes)
print(f"Mes con menor desempeño: Mes {peor_mes + 1}")

# Filtra
superiores_promedio = matriz_desempeno[matriz_desempeno > prom_general]
print("Valores sobre el promedio general:", superiores_promedio)

matriz_filtrada = np.where(matriz_desempeno < 70, 0, matriz_desempeno)
print("Matriz con valores < 70 reemplazados por 0:\n", matriz_filtrada)


print("\n--- PARTE 2: Gestión de Datos (Pandas) ---")
df = pd.DataFrame({
    "ID": [1,2,3,4,5,6],
    "Producto": ["Laptop","Mouse","Teclado","Monitor","Silla","Escritorio"],
    "Categoria": ["Tecnología","Tecnología","Tecnología","Tecnología","Hogar","Hogar"],
    "Precio": [800,20,50,300,120,250],
    "Cantidad": [5,50,30,10,15,8],
    "Sucursal": ["Norte","Sur","Centro","Norte","Sur","Centro"]
})

# Crea Columna Ingreso = Precio * Cantidad 
df["Ingreso"] = df["Precio"] * df["Cantidad"]
print("DataFrame con Ingreso:\n", df)

# Análisis
ingreso_categoria = df.groupby("Categoria")["Ingreso"].sum()
print("Ingreso total por categoría:\n", ingreso_categoria)

ingreso_sucursal = df.groupby("Sucursal")["Ingreso"].sum()
print("Ingreso total por sucursal:\n", ingreso_sucursal)

# Agrupación
promedio_ingreso_prod = df["Ingreso"].mean()
print(f"Promedio de ingreso por producto: {promedio_ingreso_prod}")

cantidad_categoria = df.groupby("Categoria")["Cantidad"].sum()
print("Cantidad total vendida por categoría:\n", cantidad_categoria)

# Segmentación
def categorizar_venta(x):
    if x < 1000:
        return 'Bajo'
    elif x <= 3000:
        return 'Medio'
    else:
        return 'Alto'

df["Nivel_Venta"] = df["Ingreso"].apply(categorizar_venta)
print("DataFrame con Segmentación Nivel_Venta:\n", df)

# Filtrado
prod_superiores = df[df["Ingreso"] > promedio_ingreso_prod]
print("Productos con ingresos superiores al promedio:\n", prod_superiores)


print("\n--- PARTE 3 y 4: Integración y Conclusiones ---")
# Sucursal más fuerte y categoría dominante
sucursal_mas_fuerte = ingreso_sucursal.idxmax()
categoria_dominante = ingreso_categoria.idxmax()

# Output the conclusions as text
conclusiones = f"""
CONCLUSIONES:
1. ¿Qué área de la empresa tiene mejor rendimiento? 
   Basado en el desempeño de los equipos (Parte 1), el Equipo {mejor_equipo + 1} es el de mayor rendimiento, con un promedio de {prom_equipo[mejor_equipo]:.2f}.
   
2. ¿Qué sucursal presenta mayor desempeño comercial? 
   La sucursal '{sucursal_mas_fuerte}' tiene el mayor ingreso total con {ingreso_sucursal[sucursal_mas_fuerte]}.

3. ¿Existe relación entre desempeño y ventas?
   Se puede inferir si asumimos que cada equipo está ligado a una sucursal. Por ejemplo, el Equipo 3 tiene el mayor rendimiento (92.5), lo que podría asociarse a una sucursal, mientras que la sucursal 'Norte' genera los mayores ingresos (7000). 
   Para hacer esta relación formal se requiere que el cruce de datos contenga las sucursales asignadas a los equipos.

4. ¿Qué decisiones recomendarías a la gerencia? 
   A) Potenciar el abastecimiento y las promociones en la categoría '{categoria_dominante}', que actualmente domina en ventas de manera significativa.
   B) Investigar por qué el mes {peor_mes + 1} presentó una caída de desempeño en los equipos y tomar medidas correctivas (por ej. capacitaciones) para las evaluaciones que quedaron con nota bajo 70.
"""
print(conclusiones)

# Guardar csv
df.to_csv('resultados_actividad_6.csv', index=False)
