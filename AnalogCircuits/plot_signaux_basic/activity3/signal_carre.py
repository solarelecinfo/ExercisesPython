import numpy as np
import matplotlib.pyplot as plt
import math

frequence = 1
amplitude = 1
t = np.linspace(0, 2, 500)

signal_carre = amplitude * np.sign(np.sin(2 * math.pi * frequence * t))

plt.plot(t, signal_carre)
plt.title("Signal carré")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude (V)")
plt.grid(True)
plt.show()

