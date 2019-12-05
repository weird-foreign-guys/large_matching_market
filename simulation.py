import csv
from prefgen import get_preferences
from useful_deviation import count_useful_deviatiors
from csv_writer import CsvWriter


def inner_simulation(rounds, lower, upper, step, debug, logging, k, delta):
    """
    This is the function that manages the different values for which
    we should run the simulation for and also writes results to file
    as they come in
    """

    # Run the simulation for all correlation coefficients supplied
    for d in delta:
        if debug == 0 or debug == 1:
            print(f"\nRunning for ρ={d}")

        # Run the simulation for all preference ordering lengths supplied
        for pref_length in k:
            if debug == 0 or debug == 1:
                print(f"\nRunning for k={pref_length}")

            # Initialize file writer if enabled (default)
            if logging:
                writer = CsvWriter(d, pref_length, rounds, lower, upper)

            # Initialize while loop that runs the simulation for the specified amount of rounds
            current_round = 0
            while rounds == -1 or rounds > current_round:

                if debug != -1:
                    print(f"\nStarting round {current_round + 1} out of {rounds}")

                # Run the simulation for ρ and k decided by outer loop, for all n
                for n in range(max(lower, pref_length), upper, step):

                    # Create the preferences for all agents
                    male_prefs, female_prefs = get_preferences(n, pref_length, d)

                    # Run deferred acceptance and look for deviations
                    useful_deviators_cnt = count_useful_deviatiors(
                        male_prefs, female_prefs
                    )

                    # Calculate ratio of agents with useful deviations
                    ratio = useful_deviators_cnt / float(n)

                    if debug == 1 or debug == 0:
                        print(f"d={d} k={pref_length}: result n={n}: ", ratio)

                    if logging:
                        writer.write(n, ratio)

                current_round += 1


def simulation(meta, rounds, lower, upper, step, debug, logging, k, delta):
    """
    Simulation function used in main.
    This function wraps the actual simulation and controls
    whether or not it should loop for ever

    Parameters:
    meta (boolean): if true run huge datacollection 
    rounds (int): Amount of rounds, -1 for infinite loop, else is set = wanted amount of rounds, default = 1
    lower (int): start of inner loop
    upper (int): end of inner loop
    step (int): step per iteration
    debug (int): -1 no printing, 0 standard amount of printing, 1 max amount of printing, default = 0
    logging (boolean): True for writing to file, default = True
    k (int): Length of preference lists, default = 10 
    """

    if meta:
        if rounds == -1:
            raise Exception(
                "Iteration rounds is set to infinite, select a fitting amount of iterations for each k and delta"
            )
        while True:
            inner_simulation(rounds, lower, upper, step, debug, logging, k, delta)
    else:
        inner_simulation(rounds, lower, upper, step, debug, logging, k, delta)
