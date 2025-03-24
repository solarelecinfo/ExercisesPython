import numpy as np
import matplotlib.pyplot as plt

# Données
resistances_mesurees = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000])  # Résistances en kΩ
tension = np.array([4.58, 5.25, 5.56, 5.71, 5.81, 5.84, 5.85, 5.89, 5.93, 5.95])  # Tension en V
courant_A = np.array([4.6e-3, 2.6e-3, 1.8e-3, 1.4e-3, 1.1e-3, 1e-3, 0.8e-3, 0.7e-3, 0.6e-3, 0.6e-3])  # Courant en A


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