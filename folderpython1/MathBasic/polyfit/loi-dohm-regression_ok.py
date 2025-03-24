import numpy as np
import matplotlib.pyplot as plt

# Données
resistance = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Résistance en kΩ
tension = np.array([4.58, 5.25, 5.56, 5.71, 5.81, 5.84, 5.85, 5.89, 5.93, 5.95])  # Tension en V
courant_mA = np.array([4.6, 2.6, 1.8, 1.4, 1.1, 1, 0.8, 0.7, 0.6, 0.6])  # Courant en mA
courant_A = courant_mA / 1000  # Conversion en ampères

# Ajustement linéaire de la droite U = R * I
coefficients = np.polyfit(courant_A, tension, 1)

# Coefficients de la droite
pente = coefficients[0]
ordonnée_origine = coefficients[1]

# Affichage de l'équation de la droite
print(f"L'équation de la droite est : U = {pente:.2f} * I + {ordonnée_origine:.2f}")

# Tracer la droite et les points
plt.scatter(courant_A, tension, color='red', label="Points mesurés")  # Tracer les points
plt.plot(courant_A, pente * courant_A + ordonnée_origine, label=f"U = {pente:.2f} * I + {ordonnée_origine:.2f}", color='blue')  # Tracer la droite
plt.xlabel('Courant (A)')
plt.ylabel('Tension (V)')
plt.legend()
plt.show()