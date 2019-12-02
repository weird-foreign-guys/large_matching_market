from useful_deviation import count_useful_deviatiors
from prefgen import get_preferences


# Given size n and preference order length k, return ratio of useful_deviator

# generate male_prefs and female_prefs
if __name__ == "__main__":
    k = 10
    output = {}
    for n in [10, 20, 30, 40, 50]:
        male_prefs, female_prefs = get_preferences(n, k)
        #print(type(female_prefs[3]))
        useful_deviators_cnt = count_useful_deviatiors(male_prefs, female_prefs)
        ratio = useful_deviators_cnt/n
        output[n] = ratio
    print(output)
