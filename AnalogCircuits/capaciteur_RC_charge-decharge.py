import numpy as np
import matplotlib.pyplot as plt

# Paramètres du circuit
R = 1000  # résistance en ohms (1 kΩ)
C = 100e-6  # capacité en farads (100 µF)
V = 5  # tension d'alimentation en volts

# Temps (0 à 5 secondes, avec 0.001 s d'intervalle)
t = np.linspace(0, 5, 1000)

# Courbe de charge : Uc(t) = V * (1 - e^(-t/RC))
Uc_charge = V * (1 - np.exp(-t / (R * C)))

# Courbe de décharge : Uc(t) = V * e^(-t/RC)
Uc_decharge = V * np.exp(-t / (R * C))

# Tracé des courbes
plt.figure(figsize=(10, 6))
plt.plot(t, Uc_charge, label="Charge du condensateur", color='blue')
plt.plot(t, Uc_decharge, label="Décharge du condensateur", color='red')
plt.title("Charge et décharge d’un condensateur de 100 µF (R = 1 kΩ)")
plt.xlabel("Temps (s)")
plt.ylabel("Tension aux bornes du condensateur Uc (V)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()