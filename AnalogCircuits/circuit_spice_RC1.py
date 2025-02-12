import numpy as np
import matplotlib.pyplot as plt

# RC circuit parameters
R = 1.0  # resistance in ohms
C = 1.0  # capacitance in farads
V0 = 1.0  # initial voltage

# Time values for RC equation
t_values = np.linspace(0, 5, 500)
Vc_values = V0 * (1 - np.exp(-t_values / (R * C)))

# Frequency values for Bode plot
omega = np.logspace(-2, 2, 500)
H_mag = 1 / np.sqrt(1 + (R * C * omega) ** 2)
H_phase = -np.arctan(R * C * omega) * (180 / np.pi)

# Plot RC equation
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(t_values, Vc_values, label='Vc(t)')
plt.xlabel('Time')
plt.ylabel('Voltage across Capacitor')
plt.title('RC Equation of Capacitor')
plt.legend()

# Plot Bode diagram
plt.subplot(1, 2, 2)
plt.loglog(omega, H_mag)
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Magnitude (dB)')
plt.title('Bode Magnitude Plot')

plt.figure()
plt.semilogx(omega, H_phase)
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Phase (degrees)')
plt.title('Bode Phase Plot')

plt.show()