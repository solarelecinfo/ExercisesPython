import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
from scipy.integrate import odeint

# Les paramètres physiques
E = 5
R = 1000.0
C = 1e-6
tau = R * C
u0 = 0


def RC_Circuit_Charging(u, t):
    return (E - u) / (R * C)


def RC_Circuit_Discharging(u, t):
    return -u / (R * C)


fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, facecolor="#FFFFCC")
cursor = Cursor(ax, useblit=True, color='blue', linewidth=1)

# Les paramètres numériques
t_min = 0.0
t_max = 10e-3
n_t = 100
tab_t = np.linspace(t_min, t_max, n_t)
tab_t1 = tab_t + 0.01
tab_u = odeint(RC_Circuit_Charging, u0, tab_t)
tab_u1 = odeint(RC_Circuit_Discharging, E, tab_t1)
u_max = max(tab_u)

# La charge du condensateur
ax.plot(tab_t, tab_u, 'r', label='uc(t)')
ax.plot(tab_t, np.ones(100) * E, 'black', label='e(t)')
ax.plot(tab_t, E * tab_t / tau, 'b',
        label="tangente à l'origine")  # tangent line du/dt at t = 0  so E - u(0) / RC = E / RC
ax.plot(tab_t, -tab_u + E, 'green', label='ur(t)')

# La décharge du condensateur
ax.plot(tab_t1, tab_u1, 'r')
ax.plot(tab_t1, np.zeros(100), 'black')
ax.plot(tab_t1, -tab_u1 + E, 'green')

plt.xlabel('t')
plt.ylabel('u')
plt.title('Circuit en série RC')
plt.ylim(0, u_max * 1.2)
plt.legend(loc=4)

plt.show()
