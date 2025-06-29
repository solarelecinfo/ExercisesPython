import numpy as np
import matplotlib.pyplot as plt

# regression.py
x_points = np.array([1, 2, 3, 4, 5])
y_points = np.array([2, 4, 5, 4, 5])

# Utilisation de la méthode des moindres carrés pour ajuster une droite
# np.polyfit ajuste une droite (polynôme de degré 1)
coefficients = np.polyfit(x_points, y_points, 1)

# Les coefficients retournés sont [pente, ordonnée à l'origine]
pente = coefficients[0]
ordonnée_origine = coefficients[1]

# Affichage de l'équation de la droite
print(f"L'équation de la droite est : y = {pente}x + {ordonnée_origine}")

# Tracer la droite et les points
plt.scatter(x_points, y_points, color='red', label="Points mesurés")  # Tracer les points
plt.plot(x_points, pente * x_points + ordonnée_origine, label=f"y = {pente:.2f}x + {ordonnée_origine:.2f}", color='blue')  # Tracer la droite
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()