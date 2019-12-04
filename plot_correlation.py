import matplotlib.pyplot as plt
import numpy as np

def func(x):
    return np.exp(-x)


def get_data(d):
    xdata = np.linspace(-d, d, 100)
    ydata = func(xdata)

    return xdata, ydata

def subplot(index, d):

    plt.subplot(1, 3, index)
    plt.ylim(top=20, bottom=0)

    plt.plot(*get_data(d), label=f"ρ={d}")
    plt.legend()


def plot():

    subplot(1, 0.05)
    subplot(2, 1)
    subplot(3, 3)

    plt.show()



if __name__ == "__main__":
    plot()