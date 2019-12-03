from useful_deviation import count_useful_deviatiors
from prefgen import get_preferences

write_to_file = True


# Given size n and preference order length k, return ratio of useful_deviator

# generate male_prefs and female_prefs
if __name__ == "__main__":
    k = 10
    output = {}
    for n in [10, 50, 100, 300, 500, 700]:
        male_prefs, female_prefs = get_preferences(n, k)
        useful_deviators_cnt = count_useful_deviatiors(male_prefs, female_prefs)
        ratio = useful_deviators_cnt / float(n)
        output[n] = ratio
        print("result: ", ratio)
    print(output)

    if write_to_file:
        with open("da_results.csv", mode="w") as f:
            for n, ratio in output.items():
                f.write(f"{n},{ratio}\n")
