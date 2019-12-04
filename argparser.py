import argparse


def get_arguments():
    parser = argparse.ArgumentParser(
        description="Approximate Strategy-Proofness in Large 2-Sided Matching Markets"
    )

    parser.add_argument(
        "--rounds",
        "-r",
        type=int,
        default=1,
        help="Specify how many rounds the simulation should be run for, -1 for indefinitely",
    )

    parser.add_argument(
        "--pref-length",
        "-k",
        type=int,
        nargs='*',
        default=10,
        help="At what length to cap the preference orderings of the first side",
    )

    parser.add_argument(
        "--delta",
        type=int,
        nargs='*',
        default=3,
        help="What amount of correlation the simulations are run",
    )

    parser.add_argument(
        "--lower",
        "-l",
        type=int,
        required=True,
        help="What n to start the simulation with, inclusive",
    )

    parser.add_argument(
        "--upper",
        "-u",
        type=int,
        required=True,
        help="The maximum n to run the simulation to, exclusive",
    )

    parser.add_argument(
        "--step",
        "-s",
        type=int,
        default=10,
        help="How many agents to increase the market size with after completed simulation",
    )

    parser.add_argument(
        "--debug",
        "-d",
        type=int,
        choices=[-1, 0, 1],
        default=0,
        help="Set verbosity of the simulation, -1: no printing, 0: minimal amount, 1: maximal",
    )

    parser.add_argument(
        "--logging",
        type=bool,
        default=True,
        help="Whether or not results should be written to file",
    )

    parser.add_argument(
        "--plot",
        "-p",
        type=bool,
        default=False,
        help="Whether results should be plotted upon completion or not",
    )

    parser.add_argument(
        "--meta",
        "-m",
        type=bool,
        default=False,
        help="Whether simulation should run for many settings until terminated",
    )

    return parser.parse_args()
