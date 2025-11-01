import numpy as np
import matplotlib.pyplot as plt
import math

def Main():
    frequence = 1  # Hz
    amplitude = 1  # Volts
    periode = 1 / frequence
    t = np.linspace(0, 2 * periode, 500)  # 2 périodes

    signal = amplitude * np.sin(2 * math.pi * frequence * t)

    plt.plot(t, signal)
    plt.title("Signal sinusoïdal simple")
    plt.xlabel("Temps (s)")
    plt.ylabel("Amplitude (V)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    Main()