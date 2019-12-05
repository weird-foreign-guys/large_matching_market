# Deferred Acceptance Deviation Simulator for Large Markets

> Approximate strategy-proofness is the new strategy-proofness

_Final Project in CS 136: Economics and Computation, Harvard University, Fall 2019_

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Introduction

The stable marriage problem is a problem where one tries tries to match agents on one side of the market to agents on the other side, resulting in a stable match, i.e. no couple of agents can do better by matching outside the mechanism. Roth (1982) showed that no mechanism can be both stable and strategy-proof for two-sided matching problems. Markets using an unstable mechanism tend to unravel, which makes stability an important property. A solution to this problem could be somehting called approximate strategy-proofness. This is a property which is observed in large markets, wherein as the market grows, the percentage of agents who could usefully deviate shrinks. This repository contains an implementation of the deferred acceptance algorithm, as well as a lot of tooling for running simulations for how many people could usefully deviate for different sizes of the market and differing levels of correlation between agents' preferences. There is also a tool for plotting the results which are stored in the `DATA`-folder.

## Running the Code

The easisest way to get started would be to `git clone` the repository to your local machine, and then `cd large_matching_market` into the folder. Once there one can invoke the command-line tool by typing `python3 start.py [--help] [simulation | plot] [...args]`.

There are two main components of the code. The most important is the `simulation`-part, which is the code that runs simlation of matching markets and calculates the amount of agents that can usefully deviate. The other part is the `plot`ing part, which lets one plot the data that the simulation generates.

### Good commands to get started quickly

#### Quick test for k=10 delta=3 in the range [10, 100) with step length 10

`python3 start.py simulation --lower 10 --upper 100 --step 10 --rounds 1`

#### Running overnight in the lower range ([10, 400)) for a range of ks and deltas

`python3 start.py simulation --lower 10 --upper 400 --step 10 -rounds 1 -k 10 20 30 -d 0.05 3 5`
