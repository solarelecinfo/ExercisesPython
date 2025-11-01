import numpy as np
import matplotlib.pyplot as plt

frequence = 2
amplitude = 1
t = np.linspace(0, 2, 500)

signal_sin = amplitude * np.sin(2 * np.pi * frequence * t)
signal_carre = amplitude * np.sign(np.sin(2 * np.pi * frequence * t))

plt.plot(t, signal_sin, label="Sinusoïdal")
plt.plot(t, signal_carre, label="Carré", linestyle="--")
plt.title("Comparaison : sinusoïdal vs carré")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude (V)")
plt.legend()
plt.grid(True)
plt.show()
