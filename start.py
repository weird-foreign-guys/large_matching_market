from argparser import get_arguments
from simulation import simulation

if __name__ == "__main__":
    args = get_arguments()

    print("Running simulation...")

    simulation(
        rounds=args.rounds,
        lower=args.lower,
        upper=args.upper,
        step=args.step,
        debug=args.debug,
        logging=args.logging,
        plot=args.plot,
        k=args.pref_length,
    )

    print("Simulation terminated.")
