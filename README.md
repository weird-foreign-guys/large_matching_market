# Deferred Acceptance Deviation Simulator for Large Markets

> Approximate strategy-proofness is the new strategy-proofness

_Final Project in CS 136: Economics and Computation, Harvard University, Fall 2019_

## Introduction

The stable marriage problem is a problem where one tries tries to match agents on one side of the market to agents on the other side, resulting in a stable match, i.e. no couple of agents can do better by matching outside the mechanism. Roth (1982) showed that no mechanism can be both stable and strategy-proof for two-sided matching problems. Markets using an unstable mechanism tend to unravel, which makes stability an important property. A solution to this problem could be somehting called approximate strategy-proofness. This is a property which is observed in large markets, wherein as the market grows, the percentage of agents who could usefully deviate shrinks. This repository contains an implementation of the deferred acceptance algorithm, as well as a lot of tooling for running simulations for how many people could usefully deviate for different sizes of the market and differing levels of correlation between agents' preferences. There is also a tool for plotting the results which are stored in the `DATA`-folder.

## The Paper

For more in depth information about this repository, the theory behind this, our results, and further steps that could be taken, read the paper found in this repository or click [here](https://google.com).

## Running the Code

The easisest way to get started would be to `git clone` the repository to your local machine, and then `cd large_matching_market` into the folder. Once there one can invoke the command-line tool by typing `python3 start.py [--help] [simulation | plot] [...args]`.

There are two main components of the code. The most important is the `simulation`-part, which is the code that runs simlation of matching markets and calculates the amount of agents that can usefully deviate. The other part is the `plot`ing part, which lets one plot the data that the simulation generates.

### Simulation

The simulation is started by running

`python3 start.py simulation [-h] [args]`

Running with the help-flag will list all available arguments. Running without any arguments will run a very basic simulation with the market size going from n=10 to n=100 (exclusive), with a step-size of 10 and preference length of 10, and a correlation coefficient of 1.0. All of these parameteres can be changed and they are described in detail below. The command is the first, and the short-hand is in parenthesis.

- `--lower` (`-l`) - Sets the lower limit for the market size n, inclusive, defaults to 10
- `--upper` (`-u`) - Sets the upper limit for the market size n, exclusive, defaults to 100
- `--pref-length` (`-k`) - Accepts a list of different values for the length of the propsing side's preference orders, defaults to [10]
- `--correlation` (`-d`) - Accepts a list of correlation coefficients to run the simulation for, defaults to [1.0]
- `--rounds` (`-r`) - Sets the amount of times the simulation should be run for each setting of preference-length and correlation coefficient, defaults to 1

### Good commands to get started quickly

#### Quick test for k=10 delta=3 in the range [10, 100) with step length 10

`python3 start.py simulation --lower 10 --upper 100 --step 10 --rounds 1`

#### Running overnight in the lower range ([10, 400)) for a range of ks and deltas

`python3 start.py simulation --lower 10 --upper 400 --step 10 -rounds 1 -k 10 20 30 -d 0.05 3 5`
