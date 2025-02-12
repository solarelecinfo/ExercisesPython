import numpy as np
import matplotlib.pyplot as plt


def drawCurve(m, b):
    # Time values for RC equation
    t_values = np.linspace(0, 50, 100)
    Vc_values = t_values * m + b

    # Frequency values for Bode plot

    # Plot RC equation
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 1, 1)
    plt.plot(t_values, Vc_values, label='Vc(t)')
    plt.xlabel('Time')
    plt.ylabel('Voltage across source')
    plt.title('Triangular equation')
    plt.legend()

    plt.show()


def drawCurveCustom(m, b, start, stop):
    # Time values for RC equation
    t_values = np.linspace(start, stop, 100)
    Vc_values = t_values * m + b

    # Frequency values for Bode plot

    # Plot RC equation
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 1, 1)
    plt.plot(t_values, Vc_values, label='Vc(t)')
    plt.xlabel('Time')
    plt.ylabel('Voltage across source')
    plt.title('Triangular equation')
    plt.legend()

    plt.show()


def calculateM(x2, y2, x1, y1):
    m = (y2 - y1) / (x2 - x1)
    b = y2 - m * x2
    print("la pente f(x)= " + str(m) + "X" + " +" + str(b))
    return [m, b]


def Main():
    pente = calculateM(2.5, 4, 0, 0)
    drawCurve(pente[0], pente[1])
    pente = calculateM(1200, 0, 0, 12)
    drawCurveCustom(-0.01, 12, 0, 1300)

    pente = calculateM(150, 1.5, 2, 0)
    drawCurveCustom(pente[0], pente[1], 0, 150)


if __name__ == "__main__":
    Main()
