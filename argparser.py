import argparse
import constants


def add_simulation_arguments(simulation_parser):
    simulation_parser.add_argument(
        "--rounds",
        "-r",
        type=int,
        default=1,
        help="Specify how many rounds the simulation should be run for, -1 for indefinitely",
    )

    simulation_parser.add_argument(
        "--pref-length",
        "-k",
        type=int,
        nargs="*",
        default=[10],
        help="At what length to cap the preference orderings of the first side",
    )

    simulation_parser.add_argument(
        "--delta",
        "-d",
        type=float,
        nargs="*",
        default=[1],
        help="What amount of correlation the simulations are run",
    )

    simulation_parser.add_argument(
        "--lower",
        "-l",
        type=int,
        required=True,
        help="What n to start the simulation with, inclusive",
    )

    simulation_parser.add_argument(
        "--upper",
        "-u",
        type=int,
        required=True,
        help="The maximum n to run the simulation to, exclusive",
    )

    simulation_parser.add_argument(
        "--step",
        "-s",
        type=int,
        default=10,
        help="How many agents to increase the market size with after completed simulation",
    )

    simulation_parser.add_argument(
        "--debug",
        type=int,
        choices=[-1, 0, 1],
        default=0,
        help="Set verbosity of the simulation, -1: no printing, 0: minimal amount, 1: maximal",
    )

    simulation_parser.add_argument(
        "--logging",
        type=bool,
        default=True,
        help="Whether or not results should be written to file",
    )

    simulation_parser.add_argument(
        "--meta",
        "-m",
        type=bool,
        default=False,
        help="Whether simulation should run for many settings until terminated",
    )


def add_plot_arguements(plot_parser):
    plot_parser.add_argument(
        "--lower-limit",
        "-l",
        type=int,
        default=None,
        help="What x-value to start the plot for, inclusive",
    )

    plot_parser.add_argument(
        "--upper-limit",
        "-u",
        type=int,
        default=None,
        help="What x-value to end the plot for, inclusive",
    )

    plot_parser.add_argument(
        "--rho",
        "-r",
        type=float,
        nargs="*",
        default=[1.0],
        help="For what values of correlation coefficient `rho` to plot",
    )

    plot_parser.add_argument(
        "--pref-length",
        "-k",
        type=int,
        nargs="*",
        default=[10],
        help="For what values of the preference length `k` to plot",
    )


def get_arguments():
    # Create the top-level argument parser
    parser = argparse.ArgumentParser(
        description="Approximate Strategy-Proofness in Large 2-Sided Matching Markets"
    )

    # Create the object for creating subparsers
    subparsers = parser.add_subparsers(help="The available commands", dest="subcommand")

    # Create the subparser for running the simulation
    simulation_parser = subparsers.add_parser(
        constants.SIMULATION,
        help="Command for starting the deferred acceptance simulation with deviation counting",
    )

    # Add the arguments to the simulation parser
    add_simulation_arguments(simulation_parser)

    # Create the subparser for running the plotting
    plot_parser = subparsers.add_parser(
        constants.PLOT,
        help="Command for plotting the data collected into the `DATA`-folder",
    )

    # Add the arguments to the plot parser
    add_plot_arguements(plot_parser)

    return parser.parse_args()
