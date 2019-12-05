from argparser import get_arguments
from simulation import simulation
from plot import plot
import config
import constants


"""
This is the main entry-point for running the simulation code in this
repo. To get started, either type `python3 start.py --help` in a terminal
or see the documentation for the different options available and some
example commands.
"""

if __name__ == "__main__":
    # Get the arguments from the terminal that started this process
    args = get_arguments()

    # If the user typed `simulation` run the simulation
    if args.subcommand == constants.SIMULATION:

        # Set this parameter to be available from anywhere
        config.debug = args.debug
        print("Running simulation...")

        simulation(
            meta=args.meta,
            rounds=args.rounds,
            lower=args.lower,
            upper=args.upper,
            step=args.step,
            debug=args.debug,
            logging=args.logging,
            k=args.pref_length,
            delta=args.delta,
        )

        print("Simulation terminated.")

    # If the user typed `plot` run the plotting
    elif args.subcommand == constants.PLOT:
        print("Plotting...")

        plot(
            rhos=args.rho,
            pref_lengths=args.pref_length,
            lower_lim=args.lower_limit,
            upper_lim=args.upper_limit,
        )

        print("Plot terminated")
