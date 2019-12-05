import os
import glob
from collections import defaultdict
import matplotlib.pyplot as plt
from operator import itemgetter
import numpy as np


def func(x, a, b, c):
    return a * np.exp(-b * x) + c


def plot(ks=[10, 15, 20, 40], ds=[0.05, 1.0, 3.0]):
    """
    A function that collects relevant data-files and combines
    them and plots the results
    """
    os.chdir("DATA")

    for col, d in enumerate(ds, start=1):
        plt.subplot(1, len(ds), col)
        for k in ks:
            # Find all relevant files and put them in a list
            files = glob.glob(f"d={d};*k={k};*")

            # Initialize the array to hold the raw data from the files
            data = []
            for file in files:
                with open(file, mode="r") as f:
                    data.extend(map(lambda x: x[:-1].split(";"), f.readlines()))

            # Do some initial cleaning of the data before it is put into a dictionary
            data = list(map(lambda x: (int(x[0]), float(x[1].replace(",", "."))), data))

            # Initialize a dictionary to collect all results from different files
            agg_data = defaultdict(lambda: {"sum": 0, "n": 0})
            for n, percentage in data:
                agg_data[n]["sum"] += percentage
                agg_data[n]["n"] += 1

            # Aggregate the data based on the data in the dictionary
            dataseries = [(key, val["sum"] / val["n"]) for key, val in agg_data.items()]

            dataseries = sorted(dataseries, key=itemgetter(0))

            plt.plot(*zip(*dataseries), label=f"k={k}")

        plt.legend()
        plt.title(f"ρ={d}")

        plt.xlabel("n")
        plt.ylabel("D(n)/n")

    plt.show()


if __name__ == "__main__":
    plot()
