import numpy as np
import matplotlib.pyplot as plt
import math


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


def drawMultipleCourves():
    # Using Numpy to create an array X
    X = np.arange(1, 2000, 10)
    V=9

    # Assign variables to the y axis part of the curve
    y = V  / (4 * X)


    # Plotting both the curves simultaneously
    plt.plot(X, y, color='r', label='I=V/4Rx')

    # Naming the x-axis, y-axis and the whole graph
    plt.xlabel("Ohms")
    plt.ylabel("Intensité(A)")
    plt.title("I vs R courbe")

    # Adding legend, which helps us recognize the curve according to it's color
    plt.legend()

    #Valeurs de ourant
    for i, j in zip(X, y):
        print(f"R = {i} Ohms donne I = {j:.4f} A")

    # To load the display window
    plt.show()






def Main():
    drawMultipleCourves()

if __name__ == "__main__":
    Main()
