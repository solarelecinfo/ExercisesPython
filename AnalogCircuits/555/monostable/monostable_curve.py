import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor

# Capacité fixe (en Farads)
C = 270e-6  # 270 µF par exemple

# Fonction pour calculer la durée du pulse t = 1.1*R*C
def RC_pulse_duration(R, C):
    return 1.1 * R * C

# Paramètres numériques
R_min = 100   # 100 Ohms
R_max = 20e3  # 20 kOhms
n_R = 100     # nombre de points

# Tableau des résistances
R_values = np.linspace(R_min, R_max, n_R)

# Calcul des durées correspondantes
t_values = RC_pulse_duration(R_values, C)

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
cursor = Cursor(ax, useblit=True, color='blue', linewidth=1)

ax.plot(R_values, t_values, 'r', label='t(R) = 1.1 R C')
ax.set_xlabel('Résistance R (Ohms)')
ax.set_ylabel('Durée tw (secondes)')
ax.set_title('Durée du pulse tw en fonction de R avec C constant =100e-6')
ax.legend()
ax.grid(True)

plt.show()