import math
from math import pi

import numpy as np
import matplotlib.pyplot as plt


def drawCurveSinus(amplitude, dephasage_rad,legends):
    A = amplitude
    x_rad = np.arange(0, 4 * math.pi, 0.1)
    x_deg = (x_rad * 180) / math.pi
    v1 = A * np.sin(x_rad)
    v2 = A * np.sin(x_rad - dephasage_rad)
    v3 = A * np.sin(x_rad - 2 * dephasage_rad)

    plt.plot(x_deg, v1, x_deg, v2, x_deg, v3)  # Utilisez x_deg ici pour tracer en degrés

    # custom
    plt.xlabel('x values from 0 to 4pi')  # string must be enclosed with quotes '  '
    plt.ylabel('sin(x),sin(x-120),sin(x-240) ')
    plt.title('Plot of sin and cos from 0 to 4pi')
    plt.legend(legends)  # legend entries as seperate strings in a list
    plt.grid(True)
    plt.show()


def drawCurveSinusx6(amplitude1, dephasage_rad1,dephasage_rad2,legends):
    A = amplitude1
    A2= amplitude1*math.sqrt(3)

    x_rad = np.arange(0, 4 * math.pi, 0.1)
    x_deg = (x_rad * 180) / math.pi

    v1 = A * np.sin(x_rad)
    v2 = A * np.sin(x_rad - dephasage_rad1)
    v3 = A * np.sin(x_rad - 2 * dephasage_rad1)

    u12 = A2 * np.sin(x_rad+dephasage_rad2)
    u23 = A2 * np.sin(x_rad + (dephasage_rad2-((2*math.pi)/3)))
    u31 = A2 * np.sin(x_rad + (dephasage_rad2-((2*math.pi)/3)*2))

    plt.plot(x_deg, v1, x_deg, v2, x_deg, v3,x_deg, u12, x_deg, u23, x_deg, u31)  # Utilisez x_deg ici pour tracer en degrés

    # custom
    plt.xlabel('x values from 0 to 4pi')  # string must be enclosed with quotes '  '
    plt.ylabel('sin(x),sin(x-120),sin(x-240) et sin(x+30),sin(x-90),sin(x-210)')
    plt.title('Plot of sin and cos from 0 to 4pi')
    plt.legend(legends)  # legend entries as seperate strings in a list
    plt.grid(True)
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
    voltage_peak = 230 * math.sqrt(2)
    dephasage_signal = (2 * math.pi) / 3
    legends=['vp*sin(x)', 'vp*sin(x-phase)', 'vp*sin(x-2*phase)']
    drawCurveSinus(voltage_peak, dephasage_signal,legends)

    #6 curbes
    voltage_peak = 230 * math.sqrt(2)
    dephasage_signal = (2 * math.pi) / 3
    dephasage_signal2 = ( math.pi) / 6
    legends=['vp*sin(x)', 'vp*sin(x-phase)', 'vp*sin(x-2*phase)','u12','u23','u31']
    drawCurveSinusx6(voltage_peak, dephasage_signal,dephasage_signal2,legends)


if __name__ == "__main__":
    Main()
