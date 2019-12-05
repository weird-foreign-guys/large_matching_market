# Deferred Acceptance Deviation Simulator for Large Markets

> Approximate strategy-proofness is the new strategy-proofness

_Final Project in CS 136: Economics and Computation, Harvard University, Fall 2019_

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Introduction

The stable marriage problem is a problem where one tries tries to match agents on one side of the market to agents on the other side, resulting in a stable match, i.e. no couple of agents can do better by matching outside the mechanism. Roth (1982) showed that no mechanism can be both stable and strategy-proof for two-sided matching problems. Markets using an unstable mechanism tend to unravel, which makes stability an important property. A solution to this problem could be somehting called approximate strategy-proofness. This is a property which is observed in large markets, wherein as the market grows, the percentage of agents who could usefully deviate shrinks. This repository contains an implementation of the deferred acceptance algorithm, as well as a lot of tooling for running simulations for how many people could usefully deviate for different sizes of the market and differing levels of correlation between agents' preferences. There is also a tool for plotting the results which are stored in the `DATA`-folder.

## The Paper

For more in depth information about this repository, the theory behind this, our results, and further steps that could be taken, read the paper found in this repository or click [here](https://github.com/weird-foreign-guys/large_matching_market/blob/master/Approximate_Strategy_Proofness_in_Large_Markets.pdf).

## Running the Code

The easisest way to get started would be to `git clone` the repository to your local machine, and then `cd large_matching_market` into the folder. Once there one can invoke the command-line tool by typing `python3 start.py [--help] [simulation | plot] [...args]`.

There are two main components of the code. The most important is the `simulation`-part, which is the code that runs simlation of matching markets and calculates the amount of agents that can usefully deviate. The other part is the `plot`ing part, which lets one plot the data that the simulation generates.

## Documentation

### Simulation

The simulation is started by running

`python3 start.py simulation [-h] [args]`

Running with the help-flag will list all available arguments. Running without any arguments will run a very basic simulation with the market size going from n=10 to n=100 (exclusive), with a step-size of 10 and preference length of 10, and a correlation coefficient of 1.0. All of these parameteres can be changed and they are described in detail below. For each point below, the arguemnt comes first, and the short-hand is in parenthesis, if it exists.

- `--lower` (`-l`) - Set the lower limit for the market size n, inclusive, defaults to 10
- `--upper` (`-u`) - Set the upper limit for the market size n, exclusive, defaults to 100
- `--step` (`-s`) - Set the step to increase the market size n with after simulation for specific n terminates, defaults to 10
- `--pref-length` (`-k`) - Accepts a list of different values for the length of the propsing side's preference orders, defaults to [10]
- `--correlation` (`-d`) - Accepts a list of correlation coefficients to run the simulation for, defaults to [1.0]
- `--rounds` (`-r`) - Sets the amount of times the simulation should be run for each setting of preference-length and correlation coefficient, defaults to 1
- `--debug` - Set the verbosity of the prints, -1 is no prints, 0 gives minimal information, 1 prints a lot of inner workings of DA-algorithm, defaults to 0
- `--logging` - Set whether or not results should be written to file, defaults to true (probably only useful when developing and debugging)
- `--meta` (`-m`) - If true this will make the simulation run loop through the above specified simulation indefinitely, until terminated, defaults to False

### Plotting

The plotting is started by running

`python3 start.py plot [-h] [args]`

Running with the help-flag will list all available arguments. Running without any arguments will run a very basic plot with the market size going from n=10 to n=400 (inclusive), for a correlation coefficient of 1.0 and preference length of k=10. All of these parameters can be changed and they are described in detail below. For each point below, the arguemnt comes first, and the short-hand is in parenthesis, if it exists.

- `--lower-limit` (`-l`) - Set the lower limit for the market size n (x-axis), inclusive, defaults to `None`, i.e. no lower limit
- `--upper` (`-u`) - Set the upper limit for the market size n (x-axis), inclusive, defaults to `None`, i.e. no upper limit
- `--rho` (`-r`) - Accepts a list of values of the correlation coefficient to plot for, every value gets its own subplot, defaults to [1.0]
- `--pref-length` (`-k`) - Accepts a list of values of the preference order length k to plot for, every k gets its own curve in the subplot for the same rho's, defaults to 10

## Some Examples to Get Started Quickly

### Simulation

- Running the simplest of all simulations with all settings set to their defaults

`python3 start.py simulation`

- Running a quick test, for preference ordering of length k=10 for the proposing side and correlation coefficient rho=3, in the range \[10, 100) with step length 10, for only one round:

`python3 start.py simulation --lower 10 --upper 100 --step 10 --rounds 1`

- Running a more comprehensive simulation in the lower range (from 10 to 400, inclusive) for a range of preference ordering lengtsh and correlation coefficients (stops only when terminated by `ctrl` + `c`):

`python3 start.py simulation --lower 10 --upper 401 --step 10 --rounds 1 --pref-length 10 15 20 --correlation 0.05 1 3 --meta True`

- Running a simulation for one specific preference ordering lengt k=20, and one specific preference correlation rho=1, on a long interval of n=20 to n=1000 agents, inclusive (stops only when terminated by `ctrl` + `c`):

`python3 start.py simulation --lower 20 --upper 1001 --step 10 --pref-length 20 --correlation 1 --meta True`

### Plotting

- Running the simplest of all plots with all settings set to their defaults

`python3 start.py plot`

- Plotting one graph for all data gathered for preference ordering length k=20 and for correlation coefficient rho=1:

`python3 start.py plot --pref-length 20 --rho 1`

With the data in this repo this displays something like the following:

![Exampple plot for the above command](https://github.com/weird-foreign-guys/large_matching_market/blob/master/img/example_1.png)

- Plotting three separete graphs in one row, each for a different value of the correlation coefficient rho, for a range of different preference lengths k, from market size n from 10 to 400:

`python3 start.py plot --lower-limit 10 --upper-limit 400 --pref-length 10 15 20 40 --rho 0.05 1 3`

This could look like the following:

![Exampple plot for the above command](https://github.com/weird-foreign-guys/large_matching_market/blob/master/img/example_2.png)


## Feedback, Questions and Bugs

We welcome all kinds of feedback or questions for this project. If you find bugs, please issue a bugreport using GitHub issues.
