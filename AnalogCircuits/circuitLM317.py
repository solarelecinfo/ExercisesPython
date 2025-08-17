import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor

# Tension d'entrée
Vs = 15  # Volts

# R1 est fixe
R1 = 1000  # Ohms

# R2 (ou Rload) varie de 1 à 1000 ohms
R2_values = np.linspace(1, 1000, 100)

# Formule du diviseur de tension
Vout = Vs * R2_values / (R1 + R2_values)

# Tracé
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, facecolor="#FFFFCC")
cursor = Cursor(ax, useblit=True, color='blue', linewidth=1)

ax.plot(R2_values, Vout, 'r', label='Vout (Diviseur de tension)')
ax.set_xlabel("R2 (ohms)")
ax.set_ylabel("Tension de sortie (V)")
ax.set_title("Diviseur de tension : Vout = Vs × R2 / (R1 + R2)")
ax.legend(loc='lower right')
ax.grid(True)

plt.show()
