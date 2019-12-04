import os
import glob
from collections import defaultdict
import matplotlib.pyplot as plt
from operator import itemgetter
from scipy.interpolate import spline


def func(x, a, b, c):
    return a * np.exp(-b * x) + c

def plot(ks=[10, 15, 20], ds=[1.0,]):
    os.chdir("DATA")

    for col, d in enumerate(ds, start=1):
        # plt.subplot(1, len(ds), col)
        for k in ks:
            files = glob.glob(f"d={d};*k={k};*")

            data = []

            for file in files:
                with open(file) as f:
                    data.extend(map(lambda x: x[:-1].split(";"), f.readlines()))

            data = list(map(lambda x: (int(x[0]), float(x[1].replace(",", "."))), data))

            agg_data = defaultdict(lambda: {"sum": 0, "n": 0})

            for n, percentage in data:
                agg_data[n]["sum"] += percentage
                agg_data[n]["n"] += 1

            dataseries = [(key, val["sum"] / val["n"]) for key, val in agg_data.items()]

            dataseries = sorted(dataseries, key=itemgetter(0))

            plt.plot(*zip(*dataseries))
            # plt.plot(spline(*zip(*dataseries), np.linspace(10, 300, 300)))
    plt.show()


if __name__ == "__main__":
    plot()
