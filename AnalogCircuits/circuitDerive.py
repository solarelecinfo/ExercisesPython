import numpy as np
from matplotlib import pyplot as plt


def plot_derivative():
    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111)
    ax.set_title("Differentiation example.")
    ax.set_xlabel(r'$\theta$')
    ax.set_ylabel(r'$f(\theta)$')
    start = 0.
    stop = 2 * np.pi
    steps = [1.0, 0.5]
    for step_size in steps:
        x = np.arange(start, stop, step_size)
        y = np.cos(x)
        ax.plot(x, y, label="Cos Step size = {}".format(step_size))

        y_diff = np.zeros_like(y)  # An array of zeros the same size as y.
        # Now take the difference of y for each x:
        for ix in range(0, len(y) - 1):  # Because we shift, we are one point short.
            dy = (y[ix + 1] - y[ix]) / (x[ix + 1] - x[ix])  # NOTE THE SHIFT
            # The x is given for the steps, which do not need to be equal sized.
            y_diff[ix] = dy
        y_diff[-1] = (y[-1] - y[-2]) / (x[-1] - x[-2])  # Use a backward difference for last point
        ax.plot(x, y_diff, label="Forward diff, Step size = {}".format(step_size))
        plt.show()
        # This gives the EXAcT same result as above, but faster.
        dy = np.zeros_like(y)
        dy[0:-1] = np.diff(y) / np.diff(x)
        dy[-1] = (y[-1] - y[-2]) / (x[-1] - x[-2])  # Use a backward difference for last point
        ax.plot(x, dy, label="Forward diff NP, Step size = {}".format(step_size))

    ax.legend()
def Main():
    plot_derivative()

    print("fin program")


if __name__ == "__main__":
    Main()