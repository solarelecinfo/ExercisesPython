import numpy as np
import matplotlib.pyplot as plt

# Données
resistances_mesurees = np.array([19.1, 83.6, 165, 220, 289, 375, 465, 508, 577, 701])  # Résistances en kΩ
tension = np.array([0.429, 1.765, 2.53, 2.93, 3.37, 3.78, 4.10, 4.21, 4.32, 4.63])  # Tension en V
courant_A = np.array([24.4e-3, 18.7e-3, 15.2e-3, 13.7e-3, 11.6e-3, 10e-3, 8.6e-3, 8.3e-3, 7.4e-3, 6.6e-3])  # Courant en A


# Calcul de la résistance à partir de la loi d'Ohm (R = U / I)
resistance_calculee = tension / courant_A

# Afficher la résistance mesurée et calculée pour chaque mesure
for i in range(len(resistances_mesurees)):
    print(f"Mesurée: {resistances_mesurees[i]} Ω, Calculée: {resistance_calculee[i]:.2f} Ω")

# Ajustement linéaire de la droite U = R * I  avec R resistance du systeme
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