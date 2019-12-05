import os
import glob
from collections import defaultdict
import matplotlib.pyplot as plt
from operator import itemgetter
import numpy as np
from functools import reduce


def func(x, a, b, c):
    return a * np.exp(-b * x) + c


def plot(
    pref_lengths=[10, 15, 20, 40], rhos=[0.05, 1.0, 3.0], lower_lim=None, upper_lim=None
):
    """
    A function that collects relevant data-files and combines
    them and plots the results
    """
    os.chdir("DATA")

    for col, d in enumerate(rhos, start=1):
        plt.subplot(1, len(rhos), col)
        datapoints = 0
        for k in pref_lengths:
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
                if lower_lim is not None and n < lower_lim:
                    continue
                if upper_lim is not None and upper_lim < n:
                    continue

                agg_data[n]["sum"] += percentage
                agg_data[n]["n"] += 1

            # Count all datapoints for the total count for this graph
            datapoints += reduce(lambda sum_, x: sum_ + x["n"], agg_data.values(), 0)

            # Aggregate the data based on the data in the dictionary
            dataseries = [(key, val["sum"] / val["n"]) for key, val in agg_data.items()]

            dataseries = sorted(dataseries, key=itemgetter(0))

            plt.plot(*zip(*dataseries), label=f"k={k}")

        plt.legend()
        plt.title(f"ρ={d} ({datapoints} datapoints)")

        plt.xlabel("n")
        plt.ylabel("D(n)/n")

    plt.show()


if __name__ == "__main__":
    plot()
