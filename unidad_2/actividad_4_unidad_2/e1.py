import numpy as np

data = np.arange(10, 130, 10)

# 1. Verifica: 
#        ◦ Dimensión del arreglo 
#        ◦ Tipo de dato 

print("Original data:", data)
print("Shape:", data.shape)
print("Data type:", data.dtype)


# Original data: [ 10  20  30  40  50  60  70  80  90 100 110 120]
# Shape: (12,)
#Data type: int64

# Se puede comprobar que el arreglo original es de 1 dimensión y el tipo de dato es entero (int64).


# 2. Convierte los datos en una matriz de 4 filas.

data_reshaped = data.reshape(4,3)
print("Reshaped data:", data_reshaped)
print("Shape:", data_reshaped.shape)


# Reshaped data: 
# [[ 10  20  30]
#  [ 40  50  60]
#  [ 70  80  90]
#  [100 110 120]]
# Shape: (4, 3)

# 3. Interpreta: ¿Qué podría representar cada fila?
# Cada fila podría representar un grupo de 3 valores consecutivos del arreglo original.