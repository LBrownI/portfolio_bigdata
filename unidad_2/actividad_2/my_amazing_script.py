import pandas as pd
import numpy as np

# Datos proporcionados en la actividad
data = {
    'RUT': [
        '21.344.556-7', '20.988.123-k', '22.112.443-4', '21.554.332-1', '20.776.554-9',
        '21.221.998-0', '22.443.112-5', '20.332.887-6', '21.665.443-2', '21.332.776-k',
        '22.554.110-3', '21.887.223-4', '20.443.998-1', '21.990.554-7', '22.221.334-0',
        '20.665.112-8', '21.443.887-5', '20.887.443-2', '22.332.110-k', '21.112.665-4',
        '20.554.332-9', '21.776.998-1', '22.665.221-7', '20.221.554-3', '21.332.776-k',
        '21.990.554-7', '22.112.887-4', '21.554.665-1', '20.776.332-9', '21.221.443-0'
    ],
    'Nombre': [
        'Martina', 'Benjamín', 'Sofía', 'Mateo', 'Florencia', 'Lucas', 'Isabella',
        'Joaquín', 'Agustina', 'Catalina', 'Valentina', 'Matías', 'Elena', 'Tomás',
        'Josefa', 'Diego', 'Emilia', 'Maximiliano', 'Isidora', 'Felipe', 'Antonella',
        'Samuel', 'Fernanda', 'Francisco', 'Catalina', 'Tomás', 'Maite', 'Benjamín',
        'Constanza', 'Vicente'
    ],
    'Apellido P.': [
        'Lagos', 'Oyarzún', 'Cárdenas', 'Vargas', 'Muñoz', 'Paredes', 'Barrientos',
        'Aguilar', 'Espinoza', 'Rivas', 'Ulloa', 'Gómez', 'Guerrero', 'Almonacid',
        'Villarroel', 'Jara', 'Gallardo', 'Cárcamo', 'Bórquez', 'Arriagada', 'Saldivia',
        'Carrasco', 'Henríquez', 'Orellana', 'Rivas', 'Almonacid', 'Figueroa', 'Leiva',
        'Mena', 'Pino'
    ],
    'Sexo': [
        'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'F', 'F', 'M', 'F', 'M', 'F', 'M',
        'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M'
    ],
    'Edad': [
        18, 19, 17, 18, 20, 18, 17, 21, 18, 18, 17, 18, 20, 18, 17, 19, 18, 20, 17, 18,
        19, 18, 17, 21, 18, 18, 17, 18, 20, 18
    ],
    'Ciudad': [
        'Puerto Montt', 'Osorno', 'Castro', 'Puerto Varas', 'Ancud', 'Frutillar',
        'Quellón', 'Llanquihue', 'Calbuco', 'Castro', 'Chonchi', 'Puerto Montt',
        'Osorno', 'Castro', 'Puerto Varas', 'Ancud', 'Frutillar', 'Quellón',
        'Llanquihue', 'Calbuco', 'Purranque', 'Chonchi', 'Puerto Montt', 'Osorno',
        'Castro', 'Castro', 'Ancud', 'Frutillar', 'Quellón', 'Llanquihue'
    ],
    'Promedio': [
        6.5, 5.8, 6.2, 4.5, 5.9, 6.8, 5.4, 6.1, 4.9, 6.1, 6.7, 5.5, 6.0, 4.2, 6.9, 5.7,
        6.3, 5.1, 6.6, 4.8, 5.6, 6.4, 5.3, 5.9, 6.1, 4.2, 6.8, 5.0, np.nan, 5.4
    ]
}

df = pd.DataFrame(data)

# 1. Preparar los datos: aplicar interpolación para promedios faltantes
df['Promedio'] = df['Promedio'].interpolate()

print("--- Data preparada (interpolación de promedios) ---")
print(df)

# 2. lista de alumnos mayores de 20 años de la ciudad de Puerto Montt
mayores_20_pm = df[(df['Edad'] > 20) & (df['Ciudad'] == 'Puerto Montt')]
print("\n--- Alumnos mayores de 20 en Puerto Montt ---")
print(mayores_20_pm)

# 3. listado de alumnos de sexo femenino
femeninas = df[df['Sexo'] == 'F']
print("\n--- Alumnas (Sexo Femenino) ---")
print(femeninas)

# 4. cantidad de alumnos de la ciudad de Quellón
cant_quellon = df[df['Ciudad'] == 'Quellón'].shape[0]
print(f"\nCantidad de alumnos en Quellón: {cant_quellon}")

# 5. todas las alumnas de nombre Catalina, Sara 
catalina_sara = df[(df['Sexo'] == 'F') & (df['Nombre'].isin(['Catalina', 'Sara']))]
print("\n--- Alumnas de nombre Catalina o Sara ---")
print(catalina_sara)

# 6. los alumnos que su ciudad comience con la letra P
ciudad_p = df[df['Ciudad'].str.startswith('P')]
print("\n--- Alumnos de ciudades que comienzan con 'P' ---")
print(ciudad_p)

# 7. Guardar los datos en un archivo .csv
df.to_csv('alumnos_limpio.csv', index=False)
print("\n[SUCCESS] Datos guardados en alumnos_limpio.csv")
