import numpy as np
import matplotlib.pyplot as plt
import math

# Paramètres du signal
frequence = 50      # Hz
amplitude = 9      # Volts
dephasage = math.pi / 2   # 90° en radians
periode = 1/frequence  #seconds
t = np.linspace(0, 3*periode, 500)  # 3 periodes

# Signaux
signal_sin = amplitude * np.sin(2 * math.pi * frequence * t)
signal_carre = amplitude * np.sign(np.sin(2 * math.pi * frequence * t + dephasage))

# Tracé
plt.plot(t, signal_sin, label="Sinusoïdal")
plt.plot(t, signal_carre, label="Carré (déphasé de 90°)", linestyle="--")
plt.title("Comparaison : sinusoïdal vs carré (déphasé de 90°)")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude (V)")
plt.legend()
plt.grid(True)
plt.show()