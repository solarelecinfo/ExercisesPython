import numpy as np
import matplotlib.pyplot as plt

# Constantes
beta = 100
V_CE_sat = 0.3
V_CC = 10
R_C = 100

# Courants de base en A
I_B_values = np.array([10e-6, 20e-6, 30e-6])

# VCE varie de 0 à VCC
V_CE = np.linspace(0, V_CC, 500)

plt.figure(figsize=(8,6))

for I_B in I_B_values:
    I_C_active = beta * I_B  # Ic en mode actif (fixe)
    I_C = np.minimum((V_CC - V_CE) / R_C, I_C_active)  # courant limité par droite de charge
    # En dessous de V_CE_sat, on est en saturation, Ic = droite de charge
    I_C[V_CE < V_CE_sat] = (V_CC - V_CE[V_CE < V_CE_sat]) / R_C
    plt.plot(V_CE, I_C * 1e3, label=f'I_B = {I_B*1e6:.0f} µA')

# Tracer la droite de charge
I_load = (V_CC - V_CE) / R_C
plt.plot(V_CE, I_load * 1e3, 'k--', label='Droite de charge')

plt.xlabel('V_CE (V)')
plt.ylabel('I_C (mA)')
plt.title('Caractéristique Ic vs Vce avec différents Ib')
plt.legend()
plt.grid(True)
plt.ylim(0, max(beta * I_B_values)*1e3*1.2)
plt.show()
