import numpy as np
import matplotlib.pyplot as plt

# Liste des coordonnées des points mesurés
# Par exemple, supposons que vous ayez ces points
#  I(y) vs R(x) :
x_points = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_points = np.array([4.6, 2.6, 1.8, 1.4, 1.1, 1, 0.8, 0.7, 0.6, 0.6])

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