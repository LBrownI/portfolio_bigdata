import numpy as np

data = np.arange(10, 130, 10)

data_reshaped = data.reshape(4,3)
print("Reshaped data:", data_reshaped)
print("Shape:", data_reshaped.shape)

# 1. Calcula el promedio de desempeño por equipo (filas).

average_per_team = np.mean(data_reshaped, axis=1)
print("Average performance per team:", average_per_team)

# Average performance per team: [ 20.  50.  80. 110.]

# 2. Calcula el promedio general.

overall_average = np.mean(data_reshaped)
print("Overall average:", overall_average)

# Overall average: 65.0

# 3. Identifica el equipo con mejor desempeño.
best_team_index = np.argmax(average_per_team)
print("Best team index:", best_team_index)
print("Best team average:", average_per_team[best_team_index])