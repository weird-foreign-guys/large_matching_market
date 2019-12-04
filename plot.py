import os
import glob
from collections import defaultdict
import matplotlib.pyplot as plt

# DATA/k=20;rounds=5;delta=10.txt
def plot(ks=[10, 20], delta=3):
    os.chdir("DATA")

    for k in ks:
        files = glob.glob(f"k={k};*d={delta};*")

        data = []

        for file in files:
            with open(file) as f:
                data.extend(map(lambda x: x[:-1].split(";"), f.readlines()))

        data = list(map(lambda x: (int(x[0]), float(x[1].replace(",", "."))), data))

        agg_data = defaultdict(lambda: {"sum": 0, "n": 0})

        for n, percentage in data:
            agg_data[n]["sum"] += percentage
            agg_data[n]["n"] += 1

        print(agg_data)

        dataseries = [(key, val["sum"] / val["n"]) for key, val in agg_data.items()]

        print(dataseries)

        plt.plot(*zip(*dataseries))
    plt.show()


if __name__ == "__main__":
    plot()