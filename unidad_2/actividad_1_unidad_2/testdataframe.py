import pandas as pd

# 1. Load the initial dataframe
df = pd.read_csv('dataframe1.csv')

df.columns = df.columns.str.strip()

print("Columnas detectadas:", df.columns.tolist())

df_clean = df.dropna().copy()

df_clean['Sueldo (CLP)'] = df_clean['Sueldo (CLP)'].astype(str).str.replace(r'[\$\.]', '', regex=True).astype(float)


lista_mayores_alto_sueldo = df_clean[(df_clean['Edad'] > 40) & (df_clean['Sueldo (CLP)'] > 1500000)]
print("\n--- Mayores de 40 con sueldo > 1.500.000 ---")
print(lista_mayores_alto_sueldo)


nombres_completos = df_clean['Nombre'] + " " + df_clean['Apellido Paterno'] + " " + df_clean['Apellido Materno']
print("\n--- Listado de Nombres Completos ---")
for nombre in nombres_completos:
    print(nombre)

bono_trabajadores = df_clean[['RUT']].copy()
bono_trabajadores['Bono (CLP)'] = df_clean['Sueldo (CLP)'] * 0.25
print("\n--- Bono del 25% por Trabajador ---")
print(bono_trabajadores)

df_clean.to_csv('dataframe1_clean.csv', index=False)
print("\n[SUCCESS] Clean dataframe saved as 'dataframe1_clean.csv'")