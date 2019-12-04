import csv
from prefgen import get_preferences
from useful_deviation import count_useful_deviatiors
from csv_writer import CsvWriter


def inner_simulation(rounds, lower, upper, step, debug, logging, plot, k, delta):
    for d in delta:
        if debug == 0 or debug == 1:
            print(f"running for delta={d}")
        for pref_length in k:
            if debug == 0 or debug == 1:
                print(f"running for k={pref_length}")
            if logging:
                writer = CsvWriter(d, pref_length, rounds, lower, upper)
            current_round = 0
            while rounds == -1 or rounds > current_round:

                if debug != -1:
                    print(f"\nStarting round {current_round + 1} out of {rounds}")

                for n in range(max(lower, pref_length), upper, step):
                    male_prefs, female_prefs = get_preferences(n, pref_length, d)
                    useful_deviators_cnt = count_useful_deviatiors(
                        male_prefs, female_prefs
                    )
                    ratio = useful_deviators_cnt / float(n)

                    if debug == 1 or debug == 0:
                        print(f"d={d}k={pref_length}: result n={n}: ", ratio)

                    if logging:
                        writer.write(n, ratio)
                current_round += 1


def simulation(meta, rounds, lower, upper, step, debug, logging, plot, k, delta):
    """ Simulation function used in main. 

    Parameters:
    meta (boolean): if true run huge datacollection 
    rounds (int): Amount of rounds, -1 for infinite loop, else is set = wanted amount of rounds, default = 1
    lower (int): start of inner loop
    upper (int): end of inner loop
    step (int): step per iteration
    debug (int): -1 no printing, 0 standard amount of printing, 1 max amount of printing, default = 0
    logging (boolean): True for writing to file, defualt = True
    plot (boolean): True for plotting, only true if rounds != -1, default = False
    k (int): Length of preference lists, defualt = 10 
    """

    if meta:
        if rounds == -1:
            raise Exception(
                "Iteration rounds is set to infinite, select a fitting amount of iterations for each k and delta"
            )
        while True:
            inner_simulation(rounds, lower, upper, step, debug, logging, plot, k, delta)
    else:
        inner_simulation(rounds, lower, upper, step, debug, logging, plot, k, delta)
