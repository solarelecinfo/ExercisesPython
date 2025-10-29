import control as ctrl
import matplotlib.pyplot as plt

num = [10]
den = [1, 2, 10]
H = ctrl.TransferFunction(num, den)

ctrl.bode(H, dB=True)
plt.show()