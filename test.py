from useful_deviation import count_useful_deviatiors
from prefgen import get_preferences
import time

write_to_file = True


# Given size n and preference order length k, return ratio of useful_deviator

# generate male_prefs and female_prefs
if __name__ == "__main__":
    k = 10
    output = {}
    for n in range(100, 201, 50):
        male_prefs, female_prefs = get_preferences(n, k)
        start_time = time.time()
        useful_deviators_cnt = count_useful_deviatiors(male_prefs, female_prefs)
        elapsed_time = time.time() - start_time
        print(elapsed_time)
        ratio = useful_deviators_cnt / float(n)
        output[n] = ratio
        print(f"result n={n}: ", ratio)
    print(output)

    if write_to_file:
        with open("da_results.csv", mode="w") as f:
            for n, ratio in output.items():
                f.write(f"{n},{ratio}\n")
