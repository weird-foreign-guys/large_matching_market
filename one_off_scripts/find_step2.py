import os
import glob


os.chdir("DATA")
files = glob.glob("*")


for file in files:
    with open(file, mode="r") as f:
        data = map(lambda x: x[:-1].split(";"), f.readlines())

    # Do some initial cleaning of the data before it is put into a dictionary
    data = list(map(lambda x: (int(x[0]), float(x[1].replace(",", "."))), data))

    if data[0][0] == data[1][0] - 2:
        print("found!", file)
        break

