import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Paramètres physiques
E = 5.0        # tension source (V)
R = 200.0      # résistance (Ohms)
L = 100.0      # inductance (H)

# Équation différentielle : di/dt = (E - R*i) / L
def RL_Circuit(i, t):
    return (E - R * i) / L

# Conditions initiales : courant nul
i0 = 0.0  

# Temps de simulation
t_min = 0.0
t_max = 5.0     # secondes
n_t = 500
tab_t = np.linspace(t_min, t_max, n_t)

# Résolution
tab_i = odeint(RL_Circuit, i0, tab_t).flatten()

# Tension aux bornes de R et L
uR = R * tab_i
uL = E - uR

# Constante de temps tau
tau = L / R
i_infini = E / R

# Création de 2 graphiques côte à côte
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), facecolor="#FFFFCC")

# --- Graphe 1 : tensions ---
ax1.plot(tab_t, uR, 'g', label='uR(t)')
ax1.plot(tab_t, uL, 'b', label='uL(t)')
ax1.axhline(E, color='black', linestyle='--', label='Source 5V')
ax1.set_xlabel('Temps (s)')
ax1.set_ylabel('Tension (V)')
ax1.set_title('Tensions dans le circuit RL')
ax1.legend()
ax1.grid()

# --- Graphe 2 : courant ---
ax2.plot(tab_t, tab_i, 'r', label='i(t) (courant)')
ax2.axhline(i_infini, color='black', linestyle='--', label='i_infini = E/R')
ax2.axvline(tau, color='blue', linestyle=':', label='tau = {:.2f}s'.format(tau))
ax2.set_xlabel('Temps (s)')
ax2.set_ylabel('Courant (A)')
ax2.set_title('Courant dans le circuit RL')
ax2.legend()
ax2.grid()

plt.suptitle("Réponse d’un circuit RL série (E=5V, R=200Ω, L=100H)", fontsize=14)
plt.show()
