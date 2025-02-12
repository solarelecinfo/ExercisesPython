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
    print("number of steps elements is " + str(len(steps)))
    for step_size in steps:
        x = np.arange(start, stop, step_size)
        y = np.cos(x)
        ax.plot(x, y, label="Cos Step size = {}".format(step_size))

        y_diff = np.zeros_like(y)  # An array of zeros the same size as y.
        # Now take the difference of y for each x:
        print("number of steps in Y elements is " + str(len(x)) + " X elements is " + str(len(x)))
        print("y[-1] == y[Max]==" + str(y[-1]) + "===" + str(y[len(y) - 1]))
        for i in y:
            print("value of Y is=" + str(i))
        for i in x:
            print("value of X is=" + str(i))

        for i in range(0, len(x) - 1):
            print("value of X range is=" + str(i))

        for ix in range(0, len(y) - 1):  # Because we shift, we are one point short.
            print("index ix is=     " + str(ix))
            print("value of y[ix + 1] is=" + str(y[ix + 1]))
            print("value of y[ix] is=" + str(y[ix]))

            print("value of x[ix + 1] is=" + str(x[ix + 1]))
            print("value of x[ix] is=" + str(x[ix]))
            dy = (y[ix + 1] - y[ix]) / (x[ix + 1] - x[ix])  # NOTE THE SHIFT (USE A FORWARD difference to calculate y_diff point)
            print("dy vaut=" + str(dy))
            # The x is given for the steps, which do not need to be equal sized.
            y_diff[ix] = dy
        y_diff[-1] = (y[-1] - y[-2]) / (x[-1] - x[-2])  # Use a BACKWARD difference for last point
        print("y_diff[-1] vaut=" + str(y_diff[-1]))
        print("y[-1] vaut=" + str(y[-1]) + "y[-2] vaut=" + str(y[-2]))
        print("x[-1] vaut=" + str(x[-1]) + "x[-2] vaut=" + str(x[-2]))
        ax.plot(x, y_diff, label="Forward diff, Step size = {}".format(step_size))
        #plt.show()
        # This gives the EXAcT same result as above, but faster.
        dy = np.zeros_like(y)
        dy[0:-1] = np.diff(y) / np.diff(x)
        dy[-1] = (y[-1] - y[-2]) / (x[-1] - x[-2])  # Use a BACKWARD difference for last point
        ax.plot(x, dy, label="Forward diff NP, Step size = {}".format(step_size))

    ax.legend()
    plt.show()

def Main():
    plot_derivative()

    print("fin program")
    exit()


if __name__ == "__main__":
    Main()
