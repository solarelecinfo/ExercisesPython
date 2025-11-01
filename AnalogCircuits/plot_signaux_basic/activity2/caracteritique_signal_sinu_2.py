
import numpy as np
import matplotlib.pyplot as plt
import math

def Main():
    frequence = 50  # Hz
    amplitude = 12 * math.sqrt(2)  # Volts
    dephasage = math.pi   # radians
    #dephasage = (math.pi*2)/3  # radians

    periode = 1 / frequence
    t = np.linspace(0, 3 * periode, 500)

    signal = amplitude * np.sin(2 * math.pi * frequence * t + dephasage)

    print("Caractéristiques du signal sinusoïdal :")
    print(f"  Fréquence : {frequence} Hz")
    print(f"  Période   : {periode:.3f} s")
    print(f"  Amplitude : {amplitude} V")
    print(f"  Déphasage : {dephasage:.2f} rad")

    plt.plot(t, signal)
    plt.title("Signal sinusoïdal déphasé")
    plt.xlabel("Temps (s)")
    plt.ylabel("Amplitude (V)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    Main()