import numpy as np
import matplotlib.pyplot as plt


def plotRCcircuit(vc,r,c):
    V0 = vc  # Tension finale (V)
    R = r  # Résistance (ohms)
    C = c #capacitance
    RC = r * c  # Constante de temps (s)
    t = np.linspace(0, 0.1, 10000)  # de 0 à 10 ms

    # Fonction u_c(t)
    u_c = V0 * (1 - np.exp(-t / RC))

    # Tracé
    plt.figure(figsize=(8, 5))
    plt.plot(t * 1000, u_c, label='u_c(t) = 5(1 - exp(-t/RC))', color='blue')
    plt.xlabel('Temps (ms)')
    plt.ylabel('Tension au condensateur (V)')
    plt.title('Charge du condensateur dans un circuit RC')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def Main():
   # plotRCcircuit(5, 20e3, 1e-6)
    plotRCcircuit(5, 20e3, 100e-9)

    print("fin program")
    exit()


if __name__ == "__main__":
    Main()
