import csv
from prefgen import get_preferences
from useful_deviation import count_useful_deviatiors
from csv_writer import CsvWriter


def simulation(rounds, lower, upper, step, debug, logging, plot, k):
    """ Simulation function used in main. 

    Parameters:
    rounds (int): Amount of rounds, -1 for infinite loop, else is set = wanted amount of rounds, default = 1
    lower (int): start of inner loop
    upper (int): end of inner loop
    step (int): step per iteration
    debug (int): -1 no printing, 0 standard amount of printing, 1 max amount of printing, default = 0
    logging (boolean): True for writing to file, defualt = True
    plot (boolean): True for plotting, only true if rounds != -1, default = False
    k (int): Length of preference lists, defualt = 10 
    """

    output = {}

    if logging:
        writer = CsvWriter(k, rounds, lower, upper)

    while rounds == -1 or rounds > 0:
        # debug = 0
        for n in range(lower, upper, step):
            male_prefs, female_prefs = get_preferences(n, k)
            useful_deviators_cnt = count_useful_deviatiors(male_prefs, female_prefs)
            ratio = useful_deviators_cnt / float(n)
            output[n] = ratio
            if debug == 1:
                print(f"result n={n}: ", ratio)
            if logging:
                writer.write(n, ratio)
        rounds -= 1
    print(output)

    # if write_to_file:
    #     with open("da_results.csv", mode="w") as f:
    #         for n, ratio in output.items():
    #             f.write(f"{n},{ratio}\n")
