import numpy as np
import matplotlib.pyplot as plt
import math

frequence = 100
amplitude = 5
periode = 1/frequence
t = np.linspace(0, 2*periode, 500)
dephasage = math.pi/2
#dephasage = math.pi

signal_carre = amplitude * np.sign(np.sin(2 * math.pi * frequence * t++dephasage))

plt.plot(t, signal_carre)
plt.title("Signal carré")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude (V)")
plt.grid(True)
plt.show()

