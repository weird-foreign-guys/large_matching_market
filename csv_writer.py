import datetime


class CsvWriter:
    # TODO add correlation
    def __init__(self, delta, k, rounds, lower, upper):
        self.file = f"DATA/d={delta};k={k};lower={lower};upper={upper};date={datetime.datetime.now()}"

    def write(self, n, ratio):
        ratio = "0," + str(ratio)[2:]
        with open(self.file, "a") as f:
            f.write(f"{n};{ratio}\n")


if __name__ == "__main__":
    writer = Csv_writer(10, 3, 2, 100)
    writer.write(10, 0.001)
    writer.write(12, 0.213123)
