with open("da_results.csv", mode="r") as f:
    lines = f.readlines()


for line in lines:
    num = str(line.split(",")[1][:-1])
    num = num.replace(".", ",")
    print(num)