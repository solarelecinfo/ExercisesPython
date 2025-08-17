import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Paramètres physiques
E_max = 5.0        # tension max source (V)
R = 200.0          # résistance (Ohms)
L = 100.0          # inductance (H)

# Fonction tension impulsionnelle : 5s ON, 5s OFF
def E_t(t):
    period = 10.0  # période totale (5s ON + 5s OFF)
    if t % period < 5.0:
        return E_max
    else:
        return 0.0

# Équation différentielle : di/dt = (E(t) - R*i) / L
def RL_Circuit(i, t):
    return (E_t(t) - R * i) / L

# Conditions initiales : courant nul
i0 = 0.0

# Temps de simulation
t_min = 0.0
t_max = 10.0     # simuler plusieurs cycles
n_t = 2000
tab_t = np.linspace(t_min, t_max, n_t)

# Résolution
tab_i = odeint(RL_Circuit, i0, tab_t).flatten()

# Tension aux bornes de R et L
tab_E = np.array([E_t(t) for t in tab_t])
uR = R * tab_i
uL = tab_E - uR

# Création de 2 graphiques côte à côte
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), facecolor="#FFFFCC")

# --- Graphe 1 : tensions ---
ax1.plot(tab_t, uR, 'g', label='uR(t)')
ax1.plot(tab_t, uL, 'b', label='uL(t)')
ax1.plot(tab_t, tab_E, 'k--', label='Source E(t)')
ax1.set_xlabel('Temps (s)')
ax1.set_ylabel('Tension (V)')
ax1.set_title('Tensions dans le circuit RL')
ax1.legend()
ax1.grid()

# --- Graphe 2 : courant ---
ax2.plot(tab_t, tab_i, 'r', label='i(t) (courant)')
ax2.set_xlabel('Temps (s)')
ax2.set_ylabel('Courant (A)')
ax2.set_title('Courant dans le circuit RL')
ax2.legend()
ax2.grid()

plt.suptitle("Réponse d’un circuit RL série à une impulsion 5s ON / 5s OFF", fontsize=14)
plt.show()