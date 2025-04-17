import numpy as np
import matplotlib.pyplot as plt

# regression.py
x_points = np.array([1, 2, 3, 4, 5])
y_points = np.array([50, 60, 70, 80, 90])



# Tracer la droite et les points

plt.plot(x_points, y_points, label=f"y vs x ", color='blue')  # Tracer la droite
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()